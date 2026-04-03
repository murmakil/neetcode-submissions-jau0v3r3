class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def checking(s):
            checks = []
            for word in wordDict:
                checks.append(s[:len(word)])
            for check in checks:
                if check in wordDict:
                    substr = s[len(check):]
                    if substr in wordDict  or substr == '':
                        return True
                    else:
                        if substr[0] in [word[0] for word in wordDict]:
                            return checking(substr)
                        else:
                            continue  
            return False
        return checking(s)
        