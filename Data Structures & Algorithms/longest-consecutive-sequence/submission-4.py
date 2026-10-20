class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set()
        seen = set()
        res = 0

        for i in nums:
            values.add(i)

        for j in nums:
            
            if j-1 not in values:
                count = 1
                while j+1 in values:
                    count += 1
                    seen.add(j+1)
                    j+=1
                res = max(count,res)
                
        return res 