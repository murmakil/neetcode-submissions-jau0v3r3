class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start = 0
        end = x // 2
        while start <= end:
            mid = (start+end) // 2
            number = mid * mid
            if number == x:
                return mid
            elif number > x:
                end = mid - 1
            else:
                start = mid + 1
        return end

            