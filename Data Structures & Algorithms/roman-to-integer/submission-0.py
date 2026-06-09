class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                res += roman.get(s[i])
                break
            elif roman.get(s[i+1]) > roman.get(s[i]):
                res += roman.get(s[i+1]) - roman.get(s[i])
                i += 2
            else:
                res += roman.get(s[i])
                i += 1
        return res