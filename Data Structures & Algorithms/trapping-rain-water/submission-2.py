class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer approach 
        # we will keep updating l_max and r_max while traversing
        l_max, r_max = 0, 0
        l, r, water = 0, len(height)-1, 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
            # print(f'l, r, l_max, r_max: {[l, r, l_max, r_max]}')
            if l_max < r_max:
                water += max(0, (min(l_max, r_max)-height[l]))
                l += 1
            else:
                water += max(0, (min(l_max, r_max)-height[r]))
                r -= 1
            # print(f'water: {water}')
        return water