class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        expences = sum(prices[0:2])
        if expences > money:
            return money
        else:
            return money - expences   
        