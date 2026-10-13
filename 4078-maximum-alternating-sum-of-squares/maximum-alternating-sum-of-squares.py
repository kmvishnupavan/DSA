class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = sorted(x * x for x in nums)

        n = len(squares)
        k = (n + 1) // 2

        ans = 0

        for i in range(n):
            if i < n // 2:
                ans -= squares[i]
            else:
                ans += squares[i]

        return ans