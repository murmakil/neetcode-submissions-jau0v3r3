class FreqStack:

    def __init__(self):
        self.frequency = dict()
        self.stack = []  

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.frequency:
            self.frequency[val] = [len(self.stack)-1]
        else:
            self.frequency[val].append(len(self.stack)-1)

    def pop(self) -> int:
        max_frequency = sorted(self.frequency.items(), key=lambda x: [len(x[1]), max(x[1])], reverse=True)[0][0]
        for num in reversed(self.stack):
            if num == 'isayka':
                continue
            elif num == max_frequency:
                self.stack[self.frequency[num][-1]] = 'isayka'
                self.frequency[num].pop()
                if len(self.frequency[num]) == 0:
                    del self.frequency[num]
                return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()