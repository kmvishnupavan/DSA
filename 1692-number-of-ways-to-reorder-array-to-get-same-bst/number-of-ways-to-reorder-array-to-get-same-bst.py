class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = 1
            comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            l = len(left)
            r = len(right)

            ways_left = solve(left)
            ways_right = solve(right)

            return (comb[l + r][l] * ways_left * ways_right) % MOD

        return (solve(nums) - 1) % MOD