class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 1000000007

        total = 1

        for i in range(1, 2 * k + 1):
            total = total * (n + k - i) % MOD
            total = total * pow(i, MOD - 2, MOD) % MOD

        return total