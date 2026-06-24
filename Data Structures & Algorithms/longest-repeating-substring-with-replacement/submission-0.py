class Solution:
    def needsReplacement(self, s: str, l: int, r: int, k: int) -> bool:
        freq = {}
        i = l
        while i <= r:
            freq[s[i]] = freq.get(s[i], 0) + 1
            i += 1
        max_freq = max(freq.values())
        window_size = r - l + 1
        return (window_size - max_freq) > k

    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l, r = 0, 0
        while r < len(s):
            if not self.needsReplacement(s,l,r,k):
                r += 1
            else: 
                while self.needsReplacement(s,l,r,k):
                    l += 1
            max_length = max(max_length, r - l)

        return max_length

        