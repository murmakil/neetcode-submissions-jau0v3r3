class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        while i < len(min(strs)):
            if all(s[i] == strs[0][i] for s in strs):
                res += strs[0][i]
                i += 1
            else:
                return res
        return res          
        