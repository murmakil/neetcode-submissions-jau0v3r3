from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        unique = [k for k,v in d.items() if v == 1]
        if len(unique) < k:
            return ''
        return unique[k-1]