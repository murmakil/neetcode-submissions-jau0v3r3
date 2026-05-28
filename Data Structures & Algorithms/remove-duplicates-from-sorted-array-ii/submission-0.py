class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            for num in nums[:i]:
                if nums[:i].count(num) > 2:
                    nums.remove(num)
        return len(nums)