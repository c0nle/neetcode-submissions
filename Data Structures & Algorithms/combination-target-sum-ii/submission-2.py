class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy()) # O(n)
                return
            if i >= len(nums) or total > target:
                return

            for idx in range(i,len(nums)):
                if idx > i and nums[idx] == nums[idx-1]:
                    continue
                if total + nums[i] > target:
                    break

                cur.append(nums[idx])
                dfs(idx+1,cur,total+nums[idx])
                cur.pop()
        
        dfs(0,[],0)

        return res
