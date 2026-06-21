class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_obj = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_obj.keys():
                return [diff_obj[diff][1], i]
            else:
                diff_obj[n] = [diff, i]
