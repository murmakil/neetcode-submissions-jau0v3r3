class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] >= target:
            return left
        elif nums[right] < target:
            return right+1
        elif nums[right] == target:
            return right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target and nums[mid+1] > target:
                return mid+1
            elif nums[mid+1] > target and nums[mid-1] < target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1