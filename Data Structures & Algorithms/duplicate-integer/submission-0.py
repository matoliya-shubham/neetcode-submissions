class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_set = set()
        for n in nums:
            if n in item_set:
                return True
            else: 
                item_set.add(n)
        return False