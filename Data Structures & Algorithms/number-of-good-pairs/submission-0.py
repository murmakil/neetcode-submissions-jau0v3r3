from itertools import combinations
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        d = dict()
        for num in set(nums):
            d[num] = []
            for k,v in enumerate(nums):
                if num == v:
                    d[num].append(k)
                elif v > num:
                    break
        check = [value for value in d.values() if len(value) > 1]
        cnt = 0
        for item in check:
            cnt += len(list(combinations(item, 2)))
        return cnt
        