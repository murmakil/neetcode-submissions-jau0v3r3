class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        r = [[num, nums.count(num)] for num in nums]
        r.sort(key=lambda sl: (sl[1],-sl[0]))
        return [elem[0] for elem in r]
        