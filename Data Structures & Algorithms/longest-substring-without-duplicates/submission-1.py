class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = 1
        for i in range(len(s)):
            cur = 1
            seen = {s[i]}
            for j in range(i+1,len(s)):
                if s[j] in seen:
                    break
                else:
                    cur += 1
                    seen.add(s[j])
            res = max(res,cur)
        return res