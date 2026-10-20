class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        [-1,-1,0,1,2,4]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                target = - nums[i]
                res.extend(self.twoSum(i,nums,target))

        return res

    def twoSum(self,i,nums,target):
        l,r = i+1, len(nums)-1
        res = []

        while l < r:
            sum = nums[l] + nums[r]
            if  sum == target:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif sum < target:
                l += 1
            else:
                r -= 1
            
        return res
