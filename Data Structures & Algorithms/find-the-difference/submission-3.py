from itertools import zip_longest
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        res = list(tup[1] for tup in zip_longest(s,t) if tup[0] != tup[1])
        return res[0]

        