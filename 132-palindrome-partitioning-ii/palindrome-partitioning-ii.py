class Solution:
    def minCut(self, s):
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length <= 2 or pal[left + 1][right - 1]:
                        pal[left][right] = True

        dp = [0] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i

                for j in range(1, i + 1):
                    if pal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]