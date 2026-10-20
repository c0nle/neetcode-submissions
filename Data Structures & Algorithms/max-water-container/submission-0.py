class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                posMaxVol = self.calcVol(i,j,heights)
                if(posMaxVol>maxVol):
                    maxVol = posMaxVol
        return maxVol
    
    def calcVol(self,i,j,heights):
        return abs(i-j)*min(heights[i],heights[j])
