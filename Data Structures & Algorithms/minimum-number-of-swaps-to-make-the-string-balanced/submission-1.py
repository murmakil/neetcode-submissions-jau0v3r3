class Solution:
    def minSwaps(self, s: str) -> int:
        size = 0
        for bracket in s:
            if bracket == "[":
                size += 1
            elif size > 0:
                size -= 1
        return (size+1) // 2
