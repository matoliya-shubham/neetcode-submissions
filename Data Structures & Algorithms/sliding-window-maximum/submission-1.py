class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_num = float('-inf')
        res = []
        for i in range(0, k):
            max_num = max(max_num, nums[i])
        res.append(max_num)
        for i in range(k, len(nums)):
            top = res[len(res) - 1]
            if top == nums[l]:
                max_num = float('-inf')
                for i in range(l+1, i+1):
                    max_num = max(max_num, nums[i]) 
                res.append(max_num)
            else: 
                if nums[i] <= top:
                    res.append(top)
                else:
                    res.append(nums[i])
            l += 1
        return res