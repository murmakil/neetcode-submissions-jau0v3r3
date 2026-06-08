class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            x = -int(abs(heapq.heappop(gifts)) ** (1/2))
            heapq.heappush(gifts, x)
        return abs(sum(gifts))