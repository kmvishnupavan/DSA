class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        count = [0] * 51

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] += 1

        ans = -1

        for x in range(51):
            if count[x] == 1:
                ans = x

        return ans