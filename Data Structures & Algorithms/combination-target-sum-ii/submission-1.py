class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()

        def dfs(i,cur,total):
            if total == target and tuple(cur) not in seen:
                res.append(cur.copy()) # O(n)
                seen.add(tuple(cur))
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i+1,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0,[],0)

        return res













































