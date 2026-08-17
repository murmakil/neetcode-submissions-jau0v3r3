class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            current = "".join([l for k,l in enumerate(s) if k != i])
            if current == current[::-1]:
                return True
        return False