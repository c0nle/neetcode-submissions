class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        low,high = 0,float("inf")
        seen = set(nums)
        res = 0
        
        for num in nums:
            cur = 1
            j = num
            while j+1 in seen:
                cur += 1
                j += 1
            
            res = max(res,cur)

        return res