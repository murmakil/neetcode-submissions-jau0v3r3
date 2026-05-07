class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100001
        start = 0
        while start < len(nums):
            current = []
            for num in nums[start:]:
                current.append(num)
                if sum(current) >= target:
                    res = min(len(current), res)
                    break
            start += 1
        if res == 100001:
            return 0
        return res