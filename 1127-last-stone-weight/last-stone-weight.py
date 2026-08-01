import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  
            x = -heapq.heappop(stones)  

            if y != x:
                heapq.heappush(stones, -(y - x))

        if stones:
            return -stones[0]
        return 0