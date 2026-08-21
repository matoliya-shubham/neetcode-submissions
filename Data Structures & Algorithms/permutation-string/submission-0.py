class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        while r < len(s2):
            count = dict(Counter(s1))
            for i in range(l, r+1):
                if s2[i] in count:
                    count[s2[i]] -= 1
                else:
                    break
            if all(v == 0 for v in count.values()):
                return True
            l += 1
            r += 1
        return False
