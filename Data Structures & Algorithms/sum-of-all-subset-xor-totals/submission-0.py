from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)+1):
            data = combinations(nums, i)
            for tup in data:
                current = 0
                for num in tup:
                    current ^= num
                res += current
        return res
