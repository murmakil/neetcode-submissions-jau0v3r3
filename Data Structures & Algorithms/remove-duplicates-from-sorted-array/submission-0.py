class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = 0
        prev_num = None
        i = 0
        while i < n:
            num = nums[i]
            if (prev_num is None or prev_num != num):
                nums[unique_nums] = num
                unique_nums += 1
            prev_num = num
            i += 1
        return unique_nums