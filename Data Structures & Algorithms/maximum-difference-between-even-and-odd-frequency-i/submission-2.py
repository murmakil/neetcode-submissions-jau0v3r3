class Solution:
    def maxDifference(self, s: str) -> int:
        s_set = set(list(s))
        d = dict()
        for letter in s_set:
            d[letter] = s.count(letter)
        r = sorted([[k,v] for k,v in d.items()], key=lambda x: x[1], reverse=True)
        even = [l[1] for l in r if l[1] % 2 == 0][-1]
        odd = [l[1] for l in r if l[1] % 2 != 0][0]
        return odd - even
        