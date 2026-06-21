class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for n in nums:
            num = n
            count = 0
            while num in num_set:
                count += 1
                num += 1
            max_count = max(count, max_count)
        return max_count


