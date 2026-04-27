class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for l in matrix:
            m.extend(l)
        left = 0
        right = len(m) - 1
        while left <= right:
            mid = (left+right) // 2
            if m[mid] > target:
                right = mid - 1
            elif m[mid] < target:
                left = mid + 1
            else:
              return True
        return False