class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        i = 1

        while i <= k:
            if i == k:
                return -heapq.heappop(max_heap)
            heapq.heappop(max_heap)
            i+=1