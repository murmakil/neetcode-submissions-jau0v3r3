class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        nums = [str(num) for num in nums]
        nulls = [k for k,v in enumerate(nums) if v == '0']
        if not nulls:
            return len(nums)
        res = 0
        for i in range(len(nulls)):
            a = 0
            checking = nums[::]
            for null in nulls[i:]:
                if a == k:
                    break
                checking[null] = '1'
                a += 1
            checking = ''.join(checking)
            checking = checking.split('0')
            res = max(res, len(max(checking)))
        return res