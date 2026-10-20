class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for l,char in enumerate(s2):
            r = l
            s1Freq = {}
            for c in s1:
                s1Freq[c] = s1Freq.get(c,0) + 1
            if char in s1Freq and r <= len(s2)-len(s1):
                while r < len(s2) and s1Freq.get(s2[r],0) > 0:
                    s1Freq[s2[r]] -= 1
                    r += 1
                for num in s1Freq.values():
                    if num != 0:
                        break
                else: return True
        return False

                