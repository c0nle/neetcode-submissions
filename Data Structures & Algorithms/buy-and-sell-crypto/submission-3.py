class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProf = 0

        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                prof = prices[r]-prices[l]
                maxProf = max(maxProf,prof)
        
        return maxProf