class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.wal = []

    def get(self, key: int) -> int:
        res = self.d.get(key, -1)
        if res != -1:
            if key in self.wal:
                self.wal.remove(key)
            self.wal.append(key)
        return res

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1 and self.capacity == len(self.d):
            del self.d[self.wal[0]]
            self.wal.pop(0)
        self.d[key] = value
        if key in self.wal:
            self.wal.remove(key)
        self.wal.append(key)
        
