class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        number = int("".join(digits))
        res = list(map(int, list(str(number + 1))))
        return res
        