class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heapq.heappush(heap, -n)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            rem = abs(x-y)
            if rem > 0:
                heapq.heappush(heap, -rem)
        return 0 if len(heap) == 0 else -heap[0]
