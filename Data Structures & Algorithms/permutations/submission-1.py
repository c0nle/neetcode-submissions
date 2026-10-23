class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if used[i]: continue

                cur.append(nums[i])

                used[i] = True

                dfs(cur)

                cur.pop()

                used[i] = False
        
        dfs([])

        return res
    
    [1,2,3]
    [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

