class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,cur,summe):
            if summe == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or summe > target:
                return
            
            dfs(i+1,cur,summe)
            cur.append(nums[i])
            summe += nums[i]
            dfs(i,cur,summe)
            cur.pop()
        dfs(0,[],0)
        return res