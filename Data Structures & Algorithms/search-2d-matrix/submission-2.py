class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.checkBoundaries(target,row):
                return self.binarySearch(row,target)
        return False
    def checkBoundaries(self,target,row):
        return row[0]<= target and target <= row[-1]

    def binarySearch(self,row,target):
        l = 0
        r = len(row) -1
        while l <= r:
            mid = (l+r)//2
            if target < row[mid]:
                r = mid-1
            elif target > row[mid]:
                l = mid+1
            else:
                return True

        return False