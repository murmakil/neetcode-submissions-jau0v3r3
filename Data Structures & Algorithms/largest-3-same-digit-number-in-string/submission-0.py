class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num2 = ''
        for k,v in enumerate(num):
            if k == len(num) - 1:
                num2 += v
                break
            num2 += v    
            if v != num[k+1]:
                num2 += '_'
        check = num2.split('_')
        res = max([eval(number[:3]) for number in check if len(number) >= 3], default='')
        if res == 0:
            return '000'
        return str(res)
        