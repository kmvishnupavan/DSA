from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cntDiv[g] = how many numbers are divisible by g
        cntDiv = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cntDiv[g] += freq[multiple]

        # exact[g] = number of pairs whose gcd is exactly g
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            total = cntDiv[g]
            pairs = total * (total - 1) // 2

            multiple = g * 2
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g

            exact[g] = pairs

        # prefix counts in sorted gcdPairs
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []
        for q in queries:
            # first gcd whose prefix > q
            ans.append(bisect_right(prefix, q))

        return ans