class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # max heap
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        # (remaining_freq, next_time)
        queue = deque()
        t = 0
        while queue or heap:
            t += 1
            # put cool down tasks back into heap
            if queue and queue[0][1] == t:
                task = queue.popleft()
                heapq.heappush(heap, -task[0])
            if heap:
                max_freq = -heapq.heappop(heap)
                remaining_freq = max_freq - 1
                next_time = t + n + 1
                if remaining_freq != 0:
                    queue.append((remaining_freq, next_time))
        return t
