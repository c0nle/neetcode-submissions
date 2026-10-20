class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        res = [1] * len(nums)
        prod = 1
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1: return [0]* len(nums)

        for i,num in enumerate(nums):
            if zero_cnt > 0:
                if num:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // num
        
        return res


        