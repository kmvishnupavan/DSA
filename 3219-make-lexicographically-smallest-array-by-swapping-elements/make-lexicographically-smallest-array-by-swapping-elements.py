class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        pairs = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        start = 0

        for end in range(1, n + 1):
            if end == n or pairs[end][0] - pairs[end - 1][0] > limit:
                
                group = pairs[start:end]

                values = sorted(value for value, index in group)
                indices = sorted(index for value, index in group)

                for i in range(len(group)):
                    ans[indices[i]] = values[i]

                start = end

        return ans