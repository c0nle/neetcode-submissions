class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        
        for num in nums:
            cur = 1
            j = num
            if j-1 not in seen:
                while j+1 in seen:
                    cur += 1
                    j += 1
            
            res = max(res,cur)

        return res