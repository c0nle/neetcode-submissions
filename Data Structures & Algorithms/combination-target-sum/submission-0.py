class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i,remaining):
            if remaining==0:
                res.append(subset.copy())
                return
            if remaining<0 or i>=len(nums):
                return

            subset.append(nums[i])
            dfs(i,remaining-nums[i])
            subset.pop()
            dfs(i+1,remaining)
            
        dfs(0,target)
        return res
