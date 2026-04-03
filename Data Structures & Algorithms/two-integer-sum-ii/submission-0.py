class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for k,v in enumerate(numbers):
            second = target - v
            if second in numbers:
                res.append(k+1)
                res.append(numbers.index(second) + 1)
                return res
