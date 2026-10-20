class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxVol = 0

        while i < j:
            possVol = (j-i)*min(heights[i],heights[j])
            maxVol = max(possVol,maxVol)
            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxVol