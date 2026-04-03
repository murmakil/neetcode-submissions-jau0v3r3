class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cum = 0
        d = {0: 1}
        for num in nums:
            cum += num
            diff = cum - k
            res += d.get(diff, 0)
            d[cum] = 1 + d.get(cum, 0)
        return res
        