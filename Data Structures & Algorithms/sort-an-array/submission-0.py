class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for k,v in enumerate(nums):
                if k == len(nums) - 1:
                  break
                elif v > nums[k+1]:
                  nums[k], nums[k+1] = nums[k+1], v 
        return nums           
        