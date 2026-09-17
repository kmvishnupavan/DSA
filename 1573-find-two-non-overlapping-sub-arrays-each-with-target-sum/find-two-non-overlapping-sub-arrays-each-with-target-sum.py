class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0...i-1]
        best = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0
        answer = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Check if there was a previous non-overlapping subarray
                if best[left] != float('inf'):
                    answer = min(answer, length + best[left])

                # Store the shortest valid subarray ending at right
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        if answer == float('inf'):
            return -1

        return answer