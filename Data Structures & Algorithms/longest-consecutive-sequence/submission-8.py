class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if not seen:  return 0
        res = 1
        for num in nums:
            cur = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    cur += 1
                    num += 1
            res = max(res,cur)
        return res