class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = dict(zip(list(order), [i for i in range(1, len(order)+1)]))
        s = list(s)
        first = []
        second = []
        for letter in s:
          if letter not in d:
            second.append(letter)
          else:
            first.append(letter)
        first.sort(key=lambda item: d[item])
        first.extend(second)
        return ''.join(first)