class MinStack:

    def __init__(self):
        self.d = []

    def push(self, val: int) -> None:
        self.d.append(val)
        if len(self.d) == 1:
            self.smallest = val
        else:
            if val < self.smallest:
                self.smallest = val 

    def pop(self) -> None:
        x = self.d.pop()
        if x == self.smallest and len(self.d) != 0:
            self.smallest = min(self.d)

    def top(self) -> int:
        return self.d[-1]

    def getMin(self) -> int:
        return self.smallest