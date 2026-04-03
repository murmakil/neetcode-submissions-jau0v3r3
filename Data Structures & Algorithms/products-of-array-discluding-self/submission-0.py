class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = 1
            for k,v in enumerate(nums):
                if i == k:
                    continue
                num *= v  
            res.append(num)
        return res
