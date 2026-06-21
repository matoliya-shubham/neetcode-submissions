class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n
        if(zeros > 1):
            return [0] * len(nums)
        ans = []
        for n in nums:
            if(n == 0):
                ans.append(prod)
            elif zeros: ans.append(0)
            else:
                ans.append(prod//n)
        return ans
