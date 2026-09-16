class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for n in points:
            heapq.heappush(heap, (-math.sqrt(n[0]*n[0] + n[1]*n[1]), n))
        
        while len(heap) > k:
            heapq.heappop(heap)
        return [x[1] for x in heap]