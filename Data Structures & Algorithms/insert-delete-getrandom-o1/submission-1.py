class RandomizedSet:

    def __init__(self):
        self.d = dict()

    def insert(self, val: int) -> bool:
        x = self.d.get(val, 'isayka')
        if x == 'isayka':
            self.d[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        x = self.d.get(val, 'isayka')
        if x == 'isayka':
            return False
        del self.d[val]
        return True

    def getRandom(self) -> int:
        import random as r
        return r.choice(list(self.d.values()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()