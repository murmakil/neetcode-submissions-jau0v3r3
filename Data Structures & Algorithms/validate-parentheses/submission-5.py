class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        d = {"[": "]", "(": ")", "{": "}"}
        i = 0 
        while i < len(s) - 1:
            if d.get(s[i], 0) != s[i+1]:
                break
            i += 2
        else:
          return True
        l = len(s) // 2 - 1
        r = l + 1
        while l >= 0 and r <= len(s) - 1:
            if d.get(s[l], 0) != s[r]:
                return False
            l -= 1
            r += 1
        return True