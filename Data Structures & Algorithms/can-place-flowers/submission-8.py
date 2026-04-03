class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n in (0,1)) or flowerbed[0]==1 and n == 0:
                return  True
            else:
                return False    
        s = ''
        for i in flowerbed:
            if i == 1:
                s += '_'
            s += str(i)  
        s = s.split('_') 
        for k, item in enumerate(s):
            if item == '' or '0' not in item:
                continue
            check = item.count('0') / 2
            if check == int(check):
                if k == 0 or k == len(s) - 1:
                    n = n - check
                else:
                    n = n - check + 1  
            else :
                n -= int(check)
            if n <= 0:
                return True
        return False        