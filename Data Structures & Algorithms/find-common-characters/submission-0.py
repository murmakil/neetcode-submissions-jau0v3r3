class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = [list(word) for word in words]
        res = []
        for letter in words[0]:
            for i in range(1, len(words)):
                if letter not in words[i]:
                    break
            else:
                for i in range(1, len(words)):
                    words[i].remove(letter)
                res.append(letter)
        return res