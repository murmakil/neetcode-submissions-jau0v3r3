class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for s in emails:
            s = list(s)
            if '+' in s:
                dog = s.index('@')
                plus = s.index('+')
                s[plus:dog] = []
            for letter in s:
                if letter == '@':
                    break
                elif letter == '.':
                    s.remove(letter)
            res.add(''.join(s))
        return len(res)