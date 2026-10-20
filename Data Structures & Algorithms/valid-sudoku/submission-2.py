class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row(board):
            for row in board:
                seen = set()
                for entry in row:
                    if entry not in seen:
                        if entry != ".":
                            seen.add(entry)
                    else: return False
            return True

        def column(board):
            for i in range(len(board[0])):
                seen = set()
                for j in range(len(board)):
                    entry = board[j][i]
                    if entry not in seen:
                        if entry != ".":
                            seen.add(entry)
                    else: return False
            return True
        
        def box(board):
            for i in range(0,9,3):
                for j in range(0,9,3):
                    seen = set()
                    for k in range(3):
                        for l in range(3):
                            entry = board[i+k][j+l]
                            if entry not in seen:
                                if entry != ".":
                                    seen.add(entry)
                            else: return False
            return True

        return row(board) and column(board) and box(board)