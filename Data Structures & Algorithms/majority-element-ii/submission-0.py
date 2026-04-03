class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        limit = len(nums) / 3
        res = []
        for num in nums_set:
            if nums.count(num) > limit:
                res.append(num)
        return res
        