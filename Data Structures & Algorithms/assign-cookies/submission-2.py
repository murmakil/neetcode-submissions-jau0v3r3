class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        res = 0
        length = len(g)
        for num in s:
            for greed in g:
                if num >= greed:
                    if res < length:
                        res += 1
                    else:
                        return length
                    g.remove(greed)    
                    break
        return res       
