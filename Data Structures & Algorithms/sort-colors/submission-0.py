class Solution:
    def sortColors(self, nums: List[int]) -> None:
        while nums != sorted(nums):
            for k,v in enumerate(nums):
                if k == len(nums) - 1:
                    break
                if v > nums[k+1]:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
        
        