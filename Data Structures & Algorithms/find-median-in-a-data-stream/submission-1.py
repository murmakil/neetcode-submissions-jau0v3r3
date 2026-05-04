class MedianFinder:

    def __init__(self):
       self.nums = [] 

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2:
            return float(self.nums[mid])
        return (self.nums[mid-1] + self.nums[mid]) / 2