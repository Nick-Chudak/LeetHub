class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Iterate over each row, using hashtable identify whether duplicates,
        Iterate over each column, using hashtable identift whether duplicatss,
        Iterate over each box, 0 <= i, j ,= 2, iterate over boxed""" 
        for i in range(len(board)):
            row_hash = {}
            for j in board[i]:
                row_hash[j] = 1 + row_hash.get(j, 0)
                if row_hash[j] != 1 and j != ".":
                    print("col_error")
                    return False
        for i in range(len(board)):
            col_hash = {}
            for j in range(len(board)):
                col_hash[board[j][i]] = 1 + col_hash.get(board[j][i], 0)
                if col_hash[board[j][i]] != 1 and board[j][i] != ".":
                    print("row_error")
                    return False
        for r in range(0, 8, 3):
            print(r)
            for c in range(0, 8, 3):
                i = r
                j = c
                box_hash = {}
                for i in range(i, i+3):
                    j = c
                    for j in range(j, j+3):
                        print("value " + str(board[i][j]) + " r - " + str(i), " c - " + str(j))
                        box_hash[board[i][j]] = 1 + box_hash.get(board[i][j], 0)
                        print(box_hash)
                        if box_hash[board[i][j]] != 1 and board[i][j] != ".":
                            print(board[i][j])
                            print("box_error")
                            return False
        return True

