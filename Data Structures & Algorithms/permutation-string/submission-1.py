from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        start = 0
        end = len(s1)
        while end <= len(s2):
            substr = s2[start:end]
            for l in substr:
                if substr.count(l) != d[l]:
                    break
            else:
                return True
            start += 1
            end += 1
        return False
