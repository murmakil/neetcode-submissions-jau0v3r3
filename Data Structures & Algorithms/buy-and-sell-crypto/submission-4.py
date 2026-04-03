class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        res = 0
        i = 0
        while i < len(prices) - 1:
            current = prices[i]
            check = min(prices[i+1:])
            profit = current - check
            if profit > res:
                res = profit
            i += 1
        return res