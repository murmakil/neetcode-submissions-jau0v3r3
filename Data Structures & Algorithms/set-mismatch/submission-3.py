class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for num in nums:
            if nums.count(num) == 2:
                res.append(num)
                break
        for i in range(1, len(nums)+1):
            if i != nums[i-1] and i not in nums:
                res.append(i)
                break
        return res