class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        i = 1
        while i < len(arr):
            res.append(max(arr[i:]))
            i += 1
        res.append(-1)
        return res
