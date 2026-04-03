class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        checks = []
        for i in range(len(words[0])):
            check = ''
            for word in words:
                try: 
                    check += word[i]
                except:
                    break
            checks.append(check)
        return words == checks
        