import re
import string

class WordDictionary:

    def __init__(self):
        self.d = dict()
        for letter in string.ascii_lowercase:
            self.d[letter] = []  

    def addWord(self, word: str) -> None:
        self.d[word[0]].append(word)

    def search(self, word: str) -> bool:
        if '.' not in word and word in self.d[word[0]]:
            return True
        if '.' in word:
            if word[0] != '.':
                for values in self.d[word[0]]:
                    if re.search(word, values) and len(values) == len(word):
                        return True
            else:
                for values in self.d.values():
                    for value in values:
                        if re.search(word, value) and len(value) == len(word):
                            return True
        return False
    
