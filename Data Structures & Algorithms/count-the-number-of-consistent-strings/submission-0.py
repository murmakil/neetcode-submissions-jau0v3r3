class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            check = set(word).difference(set(allowed))
            if set(word).difference(set(allowed)) == set():
                res += 1
        return res

        