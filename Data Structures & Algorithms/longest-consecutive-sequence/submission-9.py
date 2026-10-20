class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for num in seen:
            cur = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    cur += 1
                    num += 1
            res = max(res,cur)
        return res