class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return '''""'''
        res = ""
        for s in strs:
            res += s
            res += ';'
        return res[:-1]

    def decode(self, s: str) -> List[str]:
        if s == '''""''':
            return [""]
        elif s == '':
            return []
        return s.split(';')
