class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []

        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort by starting position
        arr.sort()

        starts = []
        for x in arr:
            starts.append(x[0])

        # Find first interval whose start > current end
        def find_next(end):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if starts[mid] > end:
                    right = mid
                else:
                    left = mid + 1

            return left

        nxt = [0] * n

        for i in range(n):
            nxt[i] = find_next(arr[i][1])

        # dp[i][k] = (maximum score, list of indices)
        # using intervals from i onward
        # and choosing at most k intervals

        dp = [[None] * 5 for _ in range(n + 1)]

        # If we can choose 0 intervals, score is always 0
        for i in range(n + 1):
            dp[i][0] = (0, [])

        # At the end, score is 0 for every k
        for k in range(1, 5):
            dp[n][k] = (0, [])

        # Fill DP from right to left
        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

                # Option 1: Skip this interval
                skip_score = dp[i + 1][k][0]
                skip_list = dp[i + 1][k][1]

                # Option 2: Take this interval
                next_score = dp[nxt[i]][k - 1][0]
                next_list = dp[nxt[i]][k - 1][1]

                take_score = arr[i][2] + next_score

                take_list = next_list + [arr[i][3]]
                take_list.sort()

                # Choose the better option
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_list)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_list)

                else:
                    # Same score -> lexicographically smaller indices
                    if take_list < skip_list:
                        dp[i][k] = (take_score, take_list)
                    else:
                        dp[i][k] = (skip_score, skip_list)

        return dp[0][4][1]
        