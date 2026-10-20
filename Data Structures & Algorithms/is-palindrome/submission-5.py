class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"}
        s = s.lower()
        processeds = ""
        for char in s:
            if "" + char in alphanumeric:
                processeds += "" + char
        if not processeds:  return True
        l, r = 0, len(processeds)-1
        while l <= r:
            if processeds[l] != processeds[r]:
                return False
            l += 1
            r -= 1
        return True