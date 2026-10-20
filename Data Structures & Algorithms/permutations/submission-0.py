class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        indices = set()
        def dfs(cur):
            if len(indices) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if i in indices:
                    continue
                indices.add(i)
                cur.append(nums[i])
                dfs(cur)
                indices.remove(i)
                cur.pop()
        dfs([])
        return res

