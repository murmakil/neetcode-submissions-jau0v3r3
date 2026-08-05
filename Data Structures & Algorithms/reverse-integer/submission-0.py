class Solution:
    def reverse(self, x: int) -> int:
        z = abs(x)
        reverse_number = 0
        while z > 0:
          z, y = divmod(z, 10)
          reverse_number = reverse_number * 10 + y
        if reverse_number <= -2 ** 31 or reverse_number >= 2 ** 31 -1:
            return 0
        else:
            if x < 0:
                return -reverse_number 
            return reverse_number