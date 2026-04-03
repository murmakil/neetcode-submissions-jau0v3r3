class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = ['b', 'a', 'l', 'o', 'n']
        r = []
        for letter in letters:
            r.append(text.count(letter))
        if r[2] < 2 or r[3] < 2 or 0 in r:
            return 0
        check = min(r[2], r[3]) // 2
        if all(letter >= check for letter in [r[0],r[1],r[4]]):
            return check