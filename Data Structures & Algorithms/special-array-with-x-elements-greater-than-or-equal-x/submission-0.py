from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            pos = bisect_left(nums, i)
            if len(nums[pos:]) == i:
                return i
        return -1