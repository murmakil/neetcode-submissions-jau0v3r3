class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        res = 0
        for i in range(1, n//2+1):
            res += i
            if res > n:
                return i - 1
        return i

        
        