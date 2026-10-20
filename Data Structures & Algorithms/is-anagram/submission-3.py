class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            word1[s[i]] = 1 + word1.get(s[i],0)
            word2[t[i]] = 1 + word2.get(t[i],0)
        
        return word1 == word2
        

        