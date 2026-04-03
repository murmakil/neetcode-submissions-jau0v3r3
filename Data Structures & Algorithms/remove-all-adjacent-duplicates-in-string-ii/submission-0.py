class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def prepare(s,k):
            s2 = ''
            for i, letter in enumerate(s):
                if i == len(s) - 1:
                    s2 += letter
                    break
                s2 += letter
                if letter != s[i+1]:
                    s2 += '_'
            s2 = s2.split('_') 
            for z, item in enumerate(s2):
                if len(item) > k:
                    s2.insert(z, item[:k])
                    s2.insert(z+1, item[k:])
                    s2.remove(item)
            s2 = ''.join([item for item in s2 if len(item) != k])
            if s2 == s:
                return s2
            return prepare(s2,k)
        return prepare(s,k)    
