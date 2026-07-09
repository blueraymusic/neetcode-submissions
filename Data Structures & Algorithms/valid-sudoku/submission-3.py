class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row and col
        row = len(board)
        col = len(board[0])

        for i in range(row):
            keep_col = []
            keep_row = []
            for j in range(col):            
                if board[i][j] != ".":
                    if board[i][j] in keep_row:
                        return False
                    keep_row.append(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in keep_col:
                        return False
                    keep_col.append(board[j][i])
                
            
        #matrix
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                matrix = []
                for i in range(box_row, box_row+3):
                    for j in range(box_col, box_col+3):       
                        if board[i][j] != ".":
                            if board[i][j] in matrix:
                                return False
                            matrix.append(board[i][j])
        return True
                
