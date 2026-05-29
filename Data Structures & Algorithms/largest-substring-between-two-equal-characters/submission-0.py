class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)
        for k,v in enumerate(s):
            d[v].append(k)
        check = [value for value in d.values() if len(value) >= 2]
        if not check:
            return -1
        res = 0
        for key in d.keys():
            if len(d[key]) < 2:
                continue
            current = d[key][-1] - d[key][0] - 1
            res = max(current, res)
        return res