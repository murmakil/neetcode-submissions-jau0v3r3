class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i = 0
        j = k
        while k <= len(arr):
            current = arr[i:k]
            if sum(current) / j >= threshold:
                res += 1
            i += 1
            k += 1
        return res