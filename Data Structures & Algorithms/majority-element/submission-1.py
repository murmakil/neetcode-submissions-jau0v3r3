class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        nums_set = set(nums)
        for num in nums_set:
            d[num] = nums.count(num)
        res = sorted([[k,v] for k,v in d.items()], key=lambda x: x[1], reverse=True)
        return res[0][0]    

        