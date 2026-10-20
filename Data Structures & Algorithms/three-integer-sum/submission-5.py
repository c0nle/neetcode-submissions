class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res += self.twoSum(i,nums,0-nums[i])
            seen.add(nums[i])
        return res

    def twoSum(self,i,nums,target):
        values = set()
        res = []
        seen = set()
        for j in range(i+1,len(nums)):
            if nums[j] not in seen:
                if nums[j] in values:
                    res.append([nums[i],nums[j],target-nums[j]])
                    seen.add(nums[j])
                else:
                    values.add(target-nums[j])
        return res

