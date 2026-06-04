class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            current = []
            for j in range(len(matrix)):
                current.append(matrix[j][i])
            res.append(current)
        return res