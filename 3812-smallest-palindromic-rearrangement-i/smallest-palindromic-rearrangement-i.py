class Solution:
    def smallestPalindrome(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):
            left.append(chr(ord('a') + i) * (freq[i] // 2))
            if freq[i] % 2 == 1:
                middle = chr(ord('a') + i)

        left = "".join(left)
        return left + middle + left[::-1]