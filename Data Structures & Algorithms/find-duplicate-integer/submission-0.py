class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda x: nums.count(x), reverse=True)[0]

        