class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur,summe):
            if summe == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or summe >= target:
                return
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j,cur,summe)
            cur.append(candidates[i])
            summe+=candidates[i]
            dfs(i+1,cur,summe)
            cur.pop()
        dfs(0,[],0)
        return res