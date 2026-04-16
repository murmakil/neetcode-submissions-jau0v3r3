class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.events) == 0:
            self.events.append((startTime, endTime))
            return True
        for event in self.events:
            if set(range(startTime, endTime)).intersection(set(range(event[0], event[1]))) != set():
                return False
        else:
            self.events.append((startTime, endTime))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)