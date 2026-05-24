class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row, columns in enumerate(self.matrix):
            if row < row1:
                continue
            elif row > row2:
                break
            for id, score in enumerate(columns):
                if id < col1:
                    continue
                elif id > col2:
                    break
                res += score
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)