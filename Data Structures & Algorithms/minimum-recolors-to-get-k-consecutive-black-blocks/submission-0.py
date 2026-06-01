class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        res = 101
        while k <= len(blocks):
            current = blocks[i:k]
            res = min(current.count('W'), res)
            i += 1
            k += 1
        return res