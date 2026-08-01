import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, [x, y]))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result