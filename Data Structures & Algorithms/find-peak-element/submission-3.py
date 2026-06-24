class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        i = 0
        j = 2
        while j < len(nums):
            if nums[i] < nums[i+1] > nums[j]:
                return i+1
            i += 1
            j += 1
        return len(nums) - 1