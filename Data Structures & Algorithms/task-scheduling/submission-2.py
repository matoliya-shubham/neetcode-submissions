class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        # Count frequencies
        for task in tasks:
            count[ord(task) - ord('A')] += 1
    
        # Highest frequency
        maxf = max(count)
    
        # Number of tasks having highest frequency
        maxCount = 0
    
        for i in count:
            if i == maxf:
                maxCount += 1
    
        # Minimum time forced by the most frequent tasks
        time = (maxf - 1) * (n + 1) + maxCount
    
        # We must execute at least len(tasks) tasks
        return max(len(tasks), time)
