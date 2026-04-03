class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 1
        while left < right and right <= len(s):
            sub = s[left:right]
            if len(sub) == len(set(sub)):
                if len(sub) > res:
                    res = len(sub)
                right += 1
            else:
                left += 1  
        return res