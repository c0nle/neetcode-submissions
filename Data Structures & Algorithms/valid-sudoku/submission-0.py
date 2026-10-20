class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        for i in range(len(board)):
            test = []
            if not self.checker(board[i]):
                return False
            for j in range(len(board[0])):
                test.append(board[j][i])
            if not self.checker(test):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                test = []
                for i in range(3):
                    for j in range(3):
                        test.append(board[r+i][c+j])
                if not self.checker(test):
                    return False

        return True

    def checker(self, liste: List[str]) -> bool:
        values = set()
        for i in liste:
            if i != ".":
                if i in values or int(i) > 9 or int(i) < 1:
                    return False
                else:
                    values.add(i)
        return True
