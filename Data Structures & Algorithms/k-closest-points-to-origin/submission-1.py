from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(point):
            res = sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            return res
        res = []
        for point in points:
            res.append([point, calc_distance(point)])
        res.sort(key=lambda x: x[1])
        res = list(map(lambda x: x[0], res))
        return res[:k]