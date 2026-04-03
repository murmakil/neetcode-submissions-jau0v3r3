class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = nums.count(num)
        res = sorted([[k,v] for k,v in d.items()], key=lambda x: x[1], reverse=True)
        return res[0][0]    

        