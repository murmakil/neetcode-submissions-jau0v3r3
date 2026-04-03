class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        elif num <= 3:
            return False
        start = 1
        end = num // 2
        nums = [num for num in range(start, end)]
        while start <= end:
            mid = (start+end) // 2
            square = nums[mid] * nums[mid]
            if square == num:
                return True
            elif square > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
