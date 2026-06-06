class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        res = [k for k, v in d.items() if v == 1]
        return res[0]