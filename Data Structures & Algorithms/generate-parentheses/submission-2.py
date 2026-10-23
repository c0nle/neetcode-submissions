class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(depth,cur,openCount,closeCount):
            if depth == 2*n:
                if openCount == closeCount == n:
                    res.append(cur)
                    return
                else:
                    return

            cur += "("
            dfs(depth+1,cur,openCount+1,closeCount)

            if closeCount < openCount:
                cur = cur[:-1]
                dfs(depth+1,cur+")",openCount,closeCount+1)

        
        dfs(0,"",0,0)

        return res

