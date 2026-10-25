class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = [0]*(len(nums))
        for num in nums:
            res[num] += 1

        for i,num in enumerate(res):
            if num > 1:
                return i