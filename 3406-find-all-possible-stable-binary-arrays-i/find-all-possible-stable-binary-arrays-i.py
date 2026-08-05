class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Only zeros
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1

        # Only ones
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):

                ways0 = 0
                for k in range(1, min(limit, i) + 1):
                    ways0 = (ways0 + dp1[i - k][j]) % MOD
                dp0[i][j] = ways0

                ways1 = 0
                for k in range(1, min(limit, j) + 1):
                    ways1 = (ways1 + dp0[i][j - k]) % MOD
                dp1[i][j] = ways1

        return (dp0[zero][one] + dp1[zero][one]) % MOD