class Solution:
    def check(self, nums: List[int]) -> bool:
        checking = sorted(nums)
        if nums == checking:
            return True
        for i in range(len(nums)):
            x = checking.pop(0)
            checking.append(x)
            if checking == nums:
                return True
        return False
        