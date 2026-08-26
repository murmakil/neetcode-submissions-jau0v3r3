class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        i = 0
        j = 0
        number = '0'
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
            else:
                if abbr[j].isdigit():
                    while j < len(abbr) and abbr[j].isdigit():
                        number += abbr[j]
                        if number == '00':
                            return False
                        j += 1
                    i += int(number)
                    number = '0'
                    if i > len(word):
                        return False
                    continue
                else:
                    return False
            j += 1
        return i == len(word) and j == len(abbr)

