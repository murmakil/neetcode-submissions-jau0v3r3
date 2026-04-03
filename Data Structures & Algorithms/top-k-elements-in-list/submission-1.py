from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        r = sorted([[k,v] for k,v in frequency.items()], key=lambda x: x[1], reverse=True)[:k]
        return  [tup[0] for tup in r]

        