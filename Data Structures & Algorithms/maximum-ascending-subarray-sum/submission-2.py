class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        s = 0
        for k,v in enumerate(nums):
            if k == len(nums) - 1:
                if nums[k-1] <= v:
                    s += v
                    if res < s:
                        res = s
                    break
                else:
                    break    
            elif v < nums[k+1]:
                s += v
            else:
                s += v
                if res < s:
                    res = s
                s = 0
        return res
