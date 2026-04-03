class Solution:
    def maxScore(self, s: str) -> int:
        delimeter = 1
        res = 0
        while delimeter <= len(s) - 1:
            left = s[:delimeter]
            right = s[delimeter:]
            current = left.count('0') + right.count('1')
            if current > res:
                res = current
            delimeter += 1
        return res
        