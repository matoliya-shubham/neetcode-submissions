class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ar = 0
        i, j = 0, len(heights)-1
        while i < j:
            area = min(heights[i], heights[j])*(j-i)
            max_ar = max(max_ar, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_ar