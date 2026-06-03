class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
            mat[i][i] = 'x'
        i = 0
        j = len(mat) - 1
        while j >= 0:
            if mat[i][j] != 'x':
                res += mat[i][j]
            i += 1
            j -= 1
        return res