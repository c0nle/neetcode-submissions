class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        seen = set()
        while l < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            res = max(r-l,res)
            if r == len(s):
                break
            while s[l] != s[r]:
                seen.remove(s[l])
                l += 1
            seen.remove(s[l])
            l += 1
        return res