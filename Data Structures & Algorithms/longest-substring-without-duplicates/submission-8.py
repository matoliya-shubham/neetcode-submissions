class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        unique = set()
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
                unique.add(s[r])
            max_len = max(max_len, len(unique))
            r += 1
        return max_len

        
