class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(depth,subSet,total):
            if total == target:
                res.append(subSet.copy())
                return
            elif depth >= len(nums) or total > target:
                return
            
            subSet.append(nums[depth])

            dfs(depth,subSet,total + nums[depth])

            subSet.pop()

            dfs(depth+1,subSet,total)
        
        dfs(0,[],0)

        return res