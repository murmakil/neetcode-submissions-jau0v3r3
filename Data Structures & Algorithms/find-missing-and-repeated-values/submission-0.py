class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r = []
        for l in grid:
            r.extend(l)
        nums = [num for num in range (1, len(grid[0]) ** 2 + 1)]
        res = []
        for num in nums:
            if r.count(num) == 2:
                res.append(num)
        for num in nums:
            if num not in r:
                res.append(num)        
        return res
