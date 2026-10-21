class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            k = (r+l) // 2
            time = 0
            for bananas in piles:
                time += math.ceil(bananas/k)
            if time <= h: 
                r = k - 1
                res = k
            else:
                l = k + 1
        return res