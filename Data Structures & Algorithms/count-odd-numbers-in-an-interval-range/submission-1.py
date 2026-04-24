class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 and high % 2:
            res = (high-low-1) // 2 + 2
        else:
            res = (high - low - 1) // 2 + 1
        return res