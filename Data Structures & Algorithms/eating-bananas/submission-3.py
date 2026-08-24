class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force approach 
        min_hr = 1
        max_hr = max(piles)
        i = min_hr
        ans = float('inf')
        l, r = 1, max_hr
        while l <= r:
            mid_num = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/mid_num)
                if total > h:
                    break
            if total <= h:
                ans = min(ans, mid_num)
                r = mid_num - 1
            else:
                l = mid_num + 1
        return ans