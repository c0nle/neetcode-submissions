class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        res = [1]*len(nums)
        for i in range(1,len(nums)):
                res[i] = res[i-1] * nums[i-1]
        suffix = 1
        for j in range(len(nums)-1,-1,-1):
                res[j] *= suffix
                suffix *= nums[j]
        return res