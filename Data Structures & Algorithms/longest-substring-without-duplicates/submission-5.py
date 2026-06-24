class Solution:
    def hasDuplicate(self, s: str, l: int, r: int) -> bool:
        str_set = set()
        i = l
        while i <= r:
            if s[i] in str_set:
                return True
            else:
                str_set.add(s[i])
            i += 1
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l, r = 0, 0
        while r < len(s):
            if not self.hasDuplicate(s,l,r):
                r += 1
            else: 
                while self.hasDuplicate(s,l,r):
                    l += 1
            max_length = max(max_length, r - l)

        return max_length
