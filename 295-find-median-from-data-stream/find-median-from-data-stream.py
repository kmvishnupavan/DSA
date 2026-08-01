import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # Max heap (store negatives)
        self.large = []  # Min heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the heaps
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

        elif len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (self.large[0] - self.small[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()