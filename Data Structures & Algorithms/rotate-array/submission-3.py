class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > len(nums):
            k = k - len(nums)
        r = len(nums) - k
        nums[r:], nums[0:r] = nums[0:r], nums[r:]
        