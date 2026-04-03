class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        d = dict()
        for letter in set(list(s)):
            d[letter] = []
            for k,v in enumerate(s):
                if v != letter:
                    continue
                d[letter].append(k)
        if len(d) == 1:
            return s
        for k, v in enumerate(d.values()):
            if len(v) == 1:
                check = s[v[0]]
                if len(check) > len(res):
                    res = check
                continue
            for i in range(len(v)):
                start = v[i]
                j = i+1
                while j < len(v):
                    end = v[j]
                    check = s[start:end+1]
                    if check == check[::-1]:
                        if len(check) > len(res):
                            res = check
                    j += 1
        return res 

