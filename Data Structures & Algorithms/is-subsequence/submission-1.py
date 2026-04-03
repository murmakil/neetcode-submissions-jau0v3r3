class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for letter in s:
            for k,v in enumerate(t):
                if letter == v:
                    t = t[k+1:]
                    break
            else:
                return False
        return True