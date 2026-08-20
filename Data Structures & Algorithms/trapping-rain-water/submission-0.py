class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force Solution
        # we will keep a map of leftmax and rightmax at everyindex
        max_heights = []
        l_max = 0
        r_max = 0
        water = 0
        for h in height:
            l_max = max(l_max, h)
            max_heights.append([l_max])
        r = len(height)-1
        while r >= 0:
            r_max = max(r_max, height[r])
            max_heights[r].append(r_max)
            r -= 1
        # water contained at any h will be equal to min(l_max, r_max) - height[i]
        for i in range(len(height)):
            water += min(max_heights[i][0], max_heights[i][1]) - height[i]

        return water