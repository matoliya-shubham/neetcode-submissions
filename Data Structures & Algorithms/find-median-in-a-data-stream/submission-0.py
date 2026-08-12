class MedianFinder:

    def __init__(self):
        self.small = [] # push -ve nums in it
        self.large = []

    def addNum(self, num: int) -> None:
        # add num to small heap first
        heapq.heappush(self.small, -num)

        # make sure every num in small heap is smaller then nums of large heap
        if self.large and -self.small[0] > self.large[0]:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # if diff in size of these heaps > 1 then balance it out
        # whichever has more element transfer it to other
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2 
        
        