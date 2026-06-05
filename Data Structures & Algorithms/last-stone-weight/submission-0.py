class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            for i, stone in enumerate(stones):
                if stone == stones[i+1]:
                    del stones[i:i+2]
                elif stones[i] > stones[i+1]:
                    stones[i] = stones[i] - stones[i+1]
                    stones.pop(i+1)
                break
        if stones:
            return stones[-1]
        return 0