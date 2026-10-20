class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()

        for i in range(len(nums)):
            if target - nums[i] in values:
                return [values.get(target - nums[i]),i]
            else:
                values[nums[i]] = i
