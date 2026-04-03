class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        reverse = list(map(lambda x: sorted(x), strs))
        res = []
        for item in reverse:
            while reverse.count(item) > 1:
                reverse.remove(item)
        for item in reverse:
            l = []
            for s in strs:
                if sorted(s) == item:
                    l.append(s)
                    res.append(l) 
        for item in res:
            while res.count(item) > 1:
                res.remove(item)             
        return res  

        