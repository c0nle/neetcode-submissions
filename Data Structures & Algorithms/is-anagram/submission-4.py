class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        if len(s) != len(t): return False

        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1
        
        for letter in t:
            if letter not in counter:
                return False
            counter[letter] -= 1
        
        for count in counter.values():
            if count != 0:
                return False
        
        return True