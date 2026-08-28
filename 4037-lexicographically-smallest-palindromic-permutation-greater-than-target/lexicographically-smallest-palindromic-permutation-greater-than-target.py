class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check palindrome possibility
        odd = -1
        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        halfCnt = [x // 2 for x in cnt]
        m = n // 2

        # Build palindrome from left half
        def build(left):
            res = left[:]

            if odd != -1:
                res.append(chr(odd + 97))

            res += left[::-1]

            return ''.join(res)

        left = [''] * m

        # Try to construct the smallest palindrome > target
        def dfs(pos, greater):
            if pos == m:
                # Decide middle character
                if odd != -1:
                    middle = chr(odd + 97)
                    candidate = ''.join(left) + middle + ''.join(left[::-1])
                else:
                    candidate = ''.join(left) + ''.join(left[::-1])

                return candidate if candidate > target else None

            # If already greater, just use smallest remaining chars
            if greater:
                for c in range(26):
                    if halfCnt[c] > 0:
                        halfCnt[c] -= 1
                        left[pos] = chr(c + 97)

                        result = dfs(pos + 1, True)

                        halfCnt[c] += 1

                        if result:
                            return result

                return None

            # We are still equal to target
            for c in range(26):
                if halfCnt[c] == 0:
                    continue

                ch = chr(c + 97)

                if ch < target[pos]:
                    continue

                halfCnt[c] -= 1
                left[pos] = ch

                if ch > target[pos]:
                    result = dfs(pos + 1, True)
                else:
                    result = dfs(pos + 1, False)

                halfCnt[c] += 1

                if result:
                    return result

            return None

        ans = dfs(0, False)

        return ans if ans else ""