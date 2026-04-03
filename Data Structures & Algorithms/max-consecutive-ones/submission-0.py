import numpy as np
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = ''
        for num in nums:
            res += str(num)
        res = res.split('0')
        return len(max(res))    
          
