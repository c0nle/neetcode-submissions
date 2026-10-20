class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.dfs(i,j,0,word,board,rows,cols):
                        return True
        return False
        
    def dfs(self,x,y,pos,word,board,rows,cols):
        if pos == len(word):
            return True

        if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != word[pos]:
            return False

        tmp = board[x][y]
        board[x][y] = "#"

        found = (
            self.dfs(x + 1, y, pos + 1, word, board, rows, cols) or
            self.dfs(x - 1, y, pos + 1, word, board, rows, cols) or
            self.dfs(x, y + 1, pos + 1, word, board, rows, cols) or
            self.dfs(x, y - 1, pos + 1, word, board, rows, cols)
        )

        board[x][y] = tmp
        return found