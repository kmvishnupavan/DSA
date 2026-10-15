class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        total = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                count = len(seen)
                total += count * count

        return total