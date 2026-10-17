class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        index = {value: i for i, value in enumerate(nums)}

        swaps = 0

        for i in range(n):
            if nums[i] != arr[i]:
                j = index[arr[i]]

                index[nums[i]] = j
                index[arr[i]] = i

                nums[i], nums[j] = nums[j], nums[i]

                swaps += 1

        return swaps