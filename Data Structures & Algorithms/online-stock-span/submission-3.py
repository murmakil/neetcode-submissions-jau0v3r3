class StockSpanner:

    def __init__(self):
        self.prices = []
        self.i = 0
                
    def next(self, price: int) -> int:
        self.i += 1
        if self.prices and self.prices[-1][0] > price:
            self.prices.append((price, self.i))
            return 1
        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
        if not self.prices:
            self.prices.append((price, self.i))
            return self.i
        self.prices.append((price, self.i))
        return self.prices[-1][1] - self.prices[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)