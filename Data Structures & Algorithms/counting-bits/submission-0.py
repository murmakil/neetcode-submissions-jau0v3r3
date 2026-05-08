class Solution:
    def countBits(self, n: int) -> List[int]:
        res = map(bin, (range(n+1)))
        res = map(lambda x: x[2:].count("1"), res)
        return list(res)

        