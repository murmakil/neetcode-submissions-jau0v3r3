from collections import deque
class LinkedList:
    
    def __init__(self):
        self.data = deque([])
    
    def get(self, index: int) -> int:
        try:
            return self.data[index]
        except:
            return -1

    def insertHead(self, val: int) -> None:
        self.data.appendleft(val)

    def insertTail(self, val: int) -> None:
        self.data.append(val)

    def remove(self, index: int) -> bool:
        num = self.get(index)
        if num == -1:
            return False
        self.data.remove(num)
        return True

    def getValues(self) -> List[int]:
        return list(self.data)
