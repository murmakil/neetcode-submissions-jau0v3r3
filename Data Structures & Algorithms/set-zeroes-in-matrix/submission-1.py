class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        for k, row in enumerate(matrix):
            for i, num in enumerate(row):
                    if num == 0:
                        zeroes.append((k,i))
        for tup in zeroes:
            matrix[tup[0]] = [0] * len(matrix[0])
            current = tup[1]
            for row in matrix:
                row[current] = 0
        
        
