class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1] and i % 2 == 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 == 1 and nums[i] <= nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
       
        