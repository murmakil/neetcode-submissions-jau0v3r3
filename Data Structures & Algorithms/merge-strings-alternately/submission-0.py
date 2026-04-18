from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = zip_longest(word1, word2, fillvalue="")
        string = ""
        for tup in res:
            tup = "".join(tup)
            string += tup
        return string