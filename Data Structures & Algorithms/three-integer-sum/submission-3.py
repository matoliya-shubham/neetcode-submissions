class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0;
        while i < len(nums) - 2:
            p1 = i+1
            p2 = len(nums) - 1
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    ans.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
            i += 1
        
        return [list(x) for x in set(tuple(sub) for sub in ans)]
                

