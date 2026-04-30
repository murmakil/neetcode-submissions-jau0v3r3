class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums2 = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums2[mid] > target:
                right = mid - 1
            elif nums2[mid] < target:
                left = mid + 1
            else:
                return nums.index(nums2[mid])
        return -1

            
        