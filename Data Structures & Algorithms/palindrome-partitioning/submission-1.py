class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(string):
            l,r = 0,len(string)-1

            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        res = []
        
        def dfs(start,cur):
            if start >= len(s):
                res.append(cur.copy())
                return

            for end in range(start,len(s)):
                subString = s[start:end+1]
                if not isPalindrome(subString):
                    continue
                cur.append(subString)
                dfs(end+1,cur)
                cur.pop()  
        
        dfs(0,[])

        return res