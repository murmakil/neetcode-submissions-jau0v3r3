class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = list(filter(lambda x: x % 2, nums))
        even = list(filter(lambda x: x % 2 == 0, nums))
        even.extend(odd)
        return even