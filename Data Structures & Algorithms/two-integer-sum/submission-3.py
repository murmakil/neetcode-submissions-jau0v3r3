class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        i = 0
        j = 1
        while i < l:
            while j < l:
                if nums[i]+ nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            else:
                i += 1
                j = i + 1    
