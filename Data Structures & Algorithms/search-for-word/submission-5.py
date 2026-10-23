class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(depth,x,y):
            if depth == len(word):
                return True
            if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board) or word[depth] != board[y][x]:
                return False
            num = board[y][x]
            board[y][x] = "#"
            res = dfs(depth+1,x+1,y) or dfs(depth+1,x-1,y) or dfs(depth+1,x,y+1) or dfs(depth+1,x,y-1)
            board[y][x] = num
            return res

        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(0,x,y): return True
        
        return False