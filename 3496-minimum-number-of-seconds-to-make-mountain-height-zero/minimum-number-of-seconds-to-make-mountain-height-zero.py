class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_finish(time):
            total = 0

            for w in workerTimes:
                left = 0
                right = mountainHeight

                while left <= right:
                    mid = (left + right) // 2

                    if w * mid * (mid + 1) // 2 <= time:
                        left = mid + 1
                    else:
                        right = mid - 1

                total += right

                if total >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left