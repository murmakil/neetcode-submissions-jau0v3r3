class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for num in set(nums):
            if nums.count(num) == 1:
                continue
            d[num] = [] 
            for i,v in enumerate(nums):
                if v == num:
                    d[num].append(i)
        for item in d.values():
            for a,b in enumerate(item):
                if a == len(item) - 1:
                    break
                res = abs(b - item[a+1])
                if res <= k:
                    return True
        return False