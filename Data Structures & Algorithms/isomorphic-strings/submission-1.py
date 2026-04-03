class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict(zip(s,t))
        if len(set(d.values())) != len(d.keys()):
            return False
        for i in range(len(s)):
            if d[s[i]] != t[i]:
                return False
        return True    
