class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(depth,subSet):
            if sum(subSet) == target:
                res.append(subSet.copy())
                return
            elif depth >= len(nums) or sum(subSet) > target:
                return
            
            subSet.append(nums[depth])

            dfs(depth,subSet)

            subSet.pop()

            dfs(depth+1,subSet)
        
        dfs(0,[])

        return res