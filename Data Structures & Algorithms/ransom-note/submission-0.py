class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
            else:
                return False 
        return True
        