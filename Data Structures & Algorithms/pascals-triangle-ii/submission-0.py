class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        current = self.getRow(rowIndex-1)
        res = [1]
        for k, num in enumerate(current):
            if k == len(current) - 1:
                break
            res.append(num + current[k+1])
        res.append(1)
        return res