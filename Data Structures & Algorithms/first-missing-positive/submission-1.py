class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(filter(lambda num: num > 0, nums)))
        if len(nums) == 0:
            return 1
        for i in range(1, len(nums)+1):
            if nums[i-1] > i:
                return i
        return nums[-1]+1