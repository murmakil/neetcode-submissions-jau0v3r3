class MyHashSet:

    def __init__(self):
        self.d = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.d.append(key)
    
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.d.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.d
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)