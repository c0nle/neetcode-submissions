class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = res = maxFreq = 0
        for r,char in enumerate(s):
            count[char] = count.get(char,0) + 1
            maxFreq = max(count.values())
            while (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res
                

            
