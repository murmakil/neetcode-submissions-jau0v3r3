class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]    

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() < self.getCapacity():
            self.arr.append(n)
        else:
            self.resize()
            self.pushback(n)      
    
    def popback(self) -> int:
        x = self.arr.pop()
        return x

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity
