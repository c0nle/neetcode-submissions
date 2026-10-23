class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(depth,subSet):
            if depth == len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[depth])

            dfs(depth+1,subSet)

            subSet.pop()

            dfs(depth+1,subSet)
        
        dfs(0,[])

        return res