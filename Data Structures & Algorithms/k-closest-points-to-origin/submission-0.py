class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            x, y = point
            d = d = x ** 2 + y ** 2
            heapq.heappush(heap, (d,point))
        
        for _ in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)
        return res
