import collections

class Solution(object):

    def __init__(self):
        self.MAX = 1000001

    def smallestPalindrome(self, s, k):
        count = collections.Counter(s)

        if not self._isPalindromePossible(count):
            return ""

        halfCount, midLetter = self._getHalfCountAndMidLetter(count)

        totalPerm = self._countArrangements(halfCount)
        if k > totalPerm:
            return ""

        leftHalf = self._generateLeftHalf(halfCount, k)

        return "".join(leftHalf) + midLetter + "".join(reversed(leftHalf))

    def _isPalindromePossible(self, count):
        odd = 0
        for v in count.values():
            if v % 2:
                odd += 1
        return odd <= 1

    def _getHalfCountAndMidLetter(self, count):
        half = [0] * 26
        mid = ""

        for ch, freq in count.items():
            half[ord(ch) - ord('a')] = freq // 2
            if freq % 2:
                mid = ch

        return half, mid

    def _generateLeftHalf(self, half, k):
        m = sum(half)
        ans = []

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self._countArrangements(half)

                if ways >= k:
                    ans.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        return ans

    def _countArrangements(self, cnt):
        total = sum(cnt)
        res = 1

        for x in cnt:
            res *= self._nCk(total, x)
            if res >= self.MAX:
                return self.MAX
            total -= x

        return res

    def _nCk(self, n, r):
        r = min(r, n - r)
        res = 1

        for i in range(1, r + 1):
            res = res * (n - r + i) // i
            if res >= self.MAX:
                return self.MAX

        return res