class Solution:
    def hasAllCharacters(self, s: str, l: int, r: int, t: str) -> bool:
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        w = s[l:r+1]
        for ch in w:
            freq[ch] = freq.get(ch, 0) - 1
        return all(v <= 0 for v in freq.values())

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif s == t:
            return s
        else:
            min_length = len(s)
            ans = ""
            l, r = 0, len(t) - 1
            while r < len(s):
                if not self.hasAllCharacters(s,l,r,t):
                    r += 1
                else: 
                    while self.hasAllCharacters(s,l,r,t):
                        str_len = r - l + 1
                        if str_len <= min_length:
                            min_length = str_len
                            ans = s[l:r+1]
                        l += 1
                    r += 1  # possible mistake (expand window after shrinking)
            
        return ans




        