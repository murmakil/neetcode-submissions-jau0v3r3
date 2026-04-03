class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            check = words[i]
            for word in words:
                if word == check:
                    continue
                else:
                    if word.find(check) != -1 and check not in res:
                        res.append(check)
            i += 1
        return res     
        