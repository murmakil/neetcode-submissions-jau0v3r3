class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end < len(nums) or start < end:
            if target < nums[start] or target > nums[end]:
                return -1
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
                if nums[start] > target:
                    return -1
            else:
                end = mid
        return -1