from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        res = [value for value in frequency.values() if value % 2]
        if len(res) == 0:
            return True
        return False    
        