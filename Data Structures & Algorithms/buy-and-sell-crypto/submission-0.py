class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProf = 0
        while r<len(prices):
            prof = prices[r]-prices[l]
            if prof <= 0:
                l = r
            else:
                maxProf = max(maxProf,prof)
            r += 1
        return maxProf

        