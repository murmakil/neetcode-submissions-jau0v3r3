class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generate_n(numRows: int) -> List[List[int]]:
            if numRows == 1:
                return [1]
            elif numRows == 2:
                return [1,1]
            current = generate_n(numRows - 1)
            res = [1]
            for k, num in enumerate(current):
                if k == len(current) - 1:
                    break
                res.append(num + current[k+1])
            res.append(1)
            return res
        
        res = []
        for i in range(1,numRows+1):
            res.append(generate_n(i))
        return res