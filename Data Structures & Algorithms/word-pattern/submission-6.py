class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if pattern == s:
            return False
        s = s.split(' ')
        d = dict()
        i = 0
        for i in range(min(len(s), len(pattern))):
            for letter in pattern[i]:
                if s[i] not in d.values():
                    d[letter] = s[i]
        check = []
        for letter in pattern:
            check.append(d.get(letter, None))
        return check == s    