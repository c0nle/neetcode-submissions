class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS,COLS = len(board),len(board[0])
        check = {1,2,3,4,5,6,7,8,9}

        for y in range(ROWS):
            seen = set()
            for x in range(COLS):
                val = board[y][x]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(board[y][x])
        
        for x in range(COLS):
            seen = set()
            for y in range(ROWS):
                val = board[y][x]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(board[y][x])
        
        for i in range(3):
            for j in range(3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        val = board[3*i+y][3*j+x]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)


        return True