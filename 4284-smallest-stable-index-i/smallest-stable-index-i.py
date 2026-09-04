class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        max_left = nums[0]

        for i in range(n):
            max_left = max(max_left, nums[i])

            if max_left - suffix_min[i] <= k:
                return i

        return -1