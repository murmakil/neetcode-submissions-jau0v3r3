class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        arr_set = sorted(set(arr), reverse=True)
        for num in arr_set:
            if arr.count(num) == num:
                return num
        return -1        

        