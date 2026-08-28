class Solution:
    def maxProduct(self, nums):
        currMax = nums[0]
        currMin = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Negative number swaps max and min
            if num < 0:
                currMax, currMin = currMin, currMax

            currMax = max(num, currMax * num)
            currMin = min(num, currMin * num)

            answer = max(answer, currMax)

        return answer