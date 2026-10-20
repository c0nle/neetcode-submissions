class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[l]<=nums[mid]<=nums[r]:
                return nums[l]
            elif nums[mid]<nums[r]:
                r = mid
            elif nums[mid] > nums[r] or nums[mid] < nums[l]:
                l = mid+1

