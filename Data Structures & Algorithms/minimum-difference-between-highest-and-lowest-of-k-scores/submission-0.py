class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        res = 100000
        while k <= len(nums):
            current = nums[i:k]
            res = min(res, current[-1] - current[0])
            i += 1
            k += 1
        return res