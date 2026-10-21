class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(mid,matrix,target):
            nums = matrix[mid]
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and mid == len(matrix) - 1 or matrix[mid][0] <= target and matrix[mid+1][0] > target:
                return binarySearch(mid,matrix,target)
            elif matrix[mid][0] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return False
