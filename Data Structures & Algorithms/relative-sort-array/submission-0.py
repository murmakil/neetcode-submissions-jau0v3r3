class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        remain = []
        for k, num in enumerate(arr2):
            d[num] = k
        for k, num in enumerate(arr1):
            if d.get(num) == None:
                arr1[k] = -1
                remain.append(num)
        remain.sort()
        arr1.sort(key=lambda x: d.get(x, 1000))
        arr1 = [num for num in arr1 if num != -1]
        arr1.extend(remain)
        return arr1