class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force Solution
        max_area = 0
        i = 0
        while i < len(heights):
            j = i+1
            while j < len(heights):
                area = (j - i) * min(heights[i], heights[j])
                max_area = max(max_area, area)
                j += 1
            i += 1
        
        return max_area