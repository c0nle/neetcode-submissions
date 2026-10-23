class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []
        
        def dfs(depth,subSet,total):
            if total == target:
                res.append(subSet.copy())
                return
                
            if depth == len(candidates) or total > target:
                return
            
            subSet.append(candidates[depth])

            dfs(depth+1,subSet,candidates[depth]+total)

            subSet.pop()

            nxt = depth + 1
            while nxt < len(candidates) and candidates[nxt] == candidates[depth]:
                nxt += 1

            dfs(nxt,subSet,total)

        dfs(0,[],0)

        return res
