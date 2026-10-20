class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","")
        s = s.lower()
        i = 0
        j = len(s)-1

        while i<=j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i] != s[j]:
                        return False
                    else:
                        i += 1
                        j -= 1
                else:
                    j-=1
            else:
                i+=1


        return True

