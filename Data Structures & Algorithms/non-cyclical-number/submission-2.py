class Solution:
    def isHappy(self, n: int) -> bool:
        def transform_n(n):
            n = list(map(int, list(str(n))))
            number = sum(map(lambda x: x * x, n))
            if number == 1:
                return True
            return number
        check = {}
        while True:
            res = transform_n(n)
            if res == 1:
                return True
            if res not in check:
                check[res] = 0
                n = res
            else:
                return False


