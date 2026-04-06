class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        mn = len(nums) // 2
        for key, value in frequency.items():
            if value > mn:
                return key
   

        