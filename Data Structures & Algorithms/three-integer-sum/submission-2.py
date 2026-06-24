class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        i = 0;
        while i < len(sorted_nums) - 2:
            p1 = i+1
            p2 = len(sorted_nums) - 1
            while p1 < p2:
                sum = sorted_nums[i] + sorted_nums[p1] + sorted_nums[p2]
                if sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    ans.append([sorted_nums[i], sorted_nums[p1], sorted_nums[p2]])
                    p1 += 1
                    p2 -= 1
            i += 1
        
        return [list(x) for x in set(tuple(sub) for sub in ans)]
                

