class StockSpanner:

    def __init__(self):
        self.prices = deque([])
                
    def next(self, price: int) -> int:
        self.prices.appendleft(price)
        span = 0
        for price in self.prices:
            if price > self.prices[0]:
                break
            span += 1
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)