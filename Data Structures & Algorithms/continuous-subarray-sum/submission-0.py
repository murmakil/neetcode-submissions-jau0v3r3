class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            s = 0
            for key, num in enumerate(nums[i:]):
                s += num
                if key == 0:
                    continue
                elif s % k == 0:
                    return True
        return False        
        