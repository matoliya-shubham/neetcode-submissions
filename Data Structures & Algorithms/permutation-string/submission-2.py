class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count1 = Counter(s1)
        window_len = len(s1)
        count2 = Counter()
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            if r-l+1 > window_len:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count1 == count2:
                return True
        return False
