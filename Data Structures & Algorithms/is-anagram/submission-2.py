class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}

        for i in s:
            if i in word:
                word[i] += 1
            else:
                word[i] = 1
        
        for j in t:
            if j in word:
                word[j] -= 1
            else:
                return False
        
        for value in word.values():
            if value != 0:
                return False
        
        return True

        