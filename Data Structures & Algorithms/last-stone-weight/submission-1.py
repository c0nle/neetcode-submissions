class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [(-stone) for stone in stones]

        stoneHeap = heapq.heapify(stones)

        stone1 = heapq.heappop(stones)
        
        while stones:
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                stone2 = -(stone2-stone1)
                heapq.heappush(stones,stone2)
            if stones:
                stone1 = heapq.heappop(stones)
            else:
                return 0
        
        return -stone1
