from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars = Counter(chars)
        for word in words:
            d = Counter(word)
            for key, value in d.items():
                if key not in chars or value > chars[key]:
                    break
            else:
                res += len(word)
        return res