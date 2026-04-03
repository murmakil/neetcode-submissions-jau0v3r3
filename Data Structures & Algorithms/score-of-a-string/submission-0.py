class Solution:
    def scoreOfString(self, s: str) -> int:
        r = []
        res = 0
        for letter in s:
            r.append(ord(letter))
        for k,v in enumerate(r):
            if k == len(r) - 1:
                break
            res += abs(r[k+1] - v)
        return res         


        