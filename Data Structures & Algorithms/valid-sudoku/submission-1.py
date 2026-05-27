class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checking_board(board):
            for row in board:
                check = set()
                for item in row:
                    if item == ".":
                        continue
                    else:
                        if item not in check:
                            check.add(item)
                        else:
                            return False
            return True
        
        if checking_board(board) == False:
            return False
        
        transpose_board = []
        for i in range(len(board[0])):
            transpose_row = []
            for row in board:
                transpose_row.append(row[i])
            transpose_board.append(transpose_row)

        if checking_board(transpose_board) == False:
            return False

        quad = []
        quad1 = board[0][0:3] + board[1][0:3] + board[2][0:3]
        quad2 = board[0][3:6] + board[1][3:6] + board[2][3:6]
        quad3 = board[0][6:9] + board[1][6:9] + board[2][6:9]
        quad4 = board[3][0:3] + board[4][0:3] + board[5][0:3]
        quad5 = board[3][3:6] + board[4][3:6] + board[5][3:6]
        quad6 = board[3][6:9] + board[4][6:9] + board[5][6:9]
        quad7 = board[6][0:3] + board[7][0:3] + board[8][0:3]
        quad8 = board[6][3:6] + board[7][3:6] + board[8][3:6]
        quad9 = board[6][6:9] + board[7][6:9] + board[8][6:9]
        quad.append([item for item in quad1 if item != "."])
        quad.append([item for item in quad2 if item != "."])
        quad.append([item for item in quad3 if item != "."])
        quad.append([item for item in quad4 if item != "."])
        quad.append([item for item in quad5 if item != "."])
        quad.append([item for item in quad6 if item != "."])
        quad.append([item for item in quad7 if item != "."])
        quad.append([item for item in quad8 if item != "."])
        quad.append([item for item in quad9 if item != "."])
        for item in quad:
            if len(item) != len(set(item)):
                return False
        return True    
        
