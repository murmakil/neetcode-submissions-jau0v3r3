class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        check = (range(x+1))
        for num in check:
            if num * num > x:
                return num - 1

            