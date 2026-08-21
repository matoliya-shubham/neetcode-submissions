class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l, r = 0, 0
        c_map = {}
        while r < len(s):
            c_map[s[r]] = c_map.get(s[r], 0) + 1
            max_freq = max(c_map.values())
            while (r - l + 1 - max_freq) > k:
                c_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len



