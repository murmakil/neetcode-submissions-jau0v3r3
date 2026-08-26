class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        i = 0
        j = 0
        number = ''
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    number += abbr[j]
                    j += 1
                i += int(number)
                number = ''
            else:
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
        return i == len(word) and j == len(abbr)

