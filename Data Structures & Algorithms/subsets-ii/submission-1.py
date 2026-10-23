class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        res = []

        def dfs(depth,cur):
            if depth == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[depth])
            
            dfs(depth+1,cur)

            cur.pop()

            nxt = depth + 1

            while nxt < len(nums) and nums[depth] == nums[nxt]:
                nxt += 1
            
            dfs(nxt,cur)
        
        dfs(0,[])

        return res