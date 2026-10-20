class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            pre *= nums[i]
            if i+1 < len(res):
                res[i+1] = pre
        
        for j in range(len(nums) -1, -1, -1):
            post *= nums[j]
            if j-1 >= 0:
                res[j-1] *= post

        return res
