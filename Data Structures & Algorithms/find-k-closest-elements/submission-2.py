class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        process = []
        for num in arr:
            process.append((num, abs(x-num)))
        sort_dict = sorted(process, key=lambda x: (x[1], x[0]))
        res = list(map(lambda pair: pair[0], sort_dict))[:k]
        res.sort()
        return res