class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(args):
            return args[-1].startswith(args[0]) and args[-1].endswith(args[0])
        res = 0
        combo = combinations(words, 2)
        for tup in combo:
            if isPrefixAndSuffix(tup):
                res += 1
        return res
