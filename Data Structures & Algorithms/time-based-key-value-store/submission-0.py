class TimeMap:

    def __init__(self):
        self.d = dict()
        self.i = -1  

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.i += 1
        self.d[self.i] = [key, value, timestamp] 

    def get(self, key: str, timestamp: int) -> str:
        for data in reversed(self.d.values()):
            if data[0] == key and data[2] <= timestamp:
                return data[1]
        return ''
