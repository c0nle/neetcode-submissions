class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = dict()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in indices:
                l = max(indices[s[r]]+1,l)
            indices[s[r]] = r
            res = max(res,r-l+1)
        return res

                