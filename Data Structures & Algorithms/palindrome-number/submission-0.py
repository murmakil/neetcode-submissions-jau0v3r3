class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse_number(x):
            rev = 0
            while x > 0:
                x,y = divmod(x, 10)
                rev = 10 * rev + y
            return rev
        return x == reverse_number(x)