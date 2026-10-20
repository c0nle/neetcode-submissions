class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(nums, i, target):
            seen = set()
            for num in nums[i+1::]:
                if target - num in seen:
                    res.add((target-num, num,nums[i]))
                seen.add(num)
            return res

        res = set()
        nums.sort()
        for i,num in enumerate(nums):
            if i < len(nums) - 1:
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                target = -num
                cur = twoSum(nums, i, target)
        return [list(t) for t in res]
