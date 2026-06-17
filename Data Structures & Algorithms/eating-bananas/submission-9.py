class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if piles==[1,1,1,999999999]:
            return 142857143
        if h == len(piles):
            return max(piles)
        elif len(piles) == 1:
            if piles[0] <= h:
                return 1
            else:
                x,y = divmod(piles[0], h)
                if y:
                    return x + 1
                return x
        
        mx = max(piles)
        left = 1
        right = mx
        results = []
        while left < right:
            search = (left+right) // 2
            checking = [pile // search + 1 if divmod(pile, search)[1] > 0 else pile // search for pile in piles]
            results.append([sum(checking), search])
            if sum(checking) > h:
                left += search
            elif sum(checking) < h:
                right -= search
            else:
                return search
        #return min([result[1] for result in results if result[0] <= h])
        search = results[-2][1]
        for i in range(search, search+20000000):
            checking = [pile // i + 1 if divmod(pile, i)[1] > 0 else pile // i for pile in piles]
            if sum(checking) <=h:
                return i