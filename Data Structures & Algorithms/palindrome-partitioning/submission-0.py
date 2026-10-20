class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(start,end):
            l,r = start, end
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start,cur):
            if start >= len(s):
                res.append(cur[::])
                return
            for end in range(start,len(s)):
                if isPalindrome(start,end):
                    cur.append(s[start:end+1])
                    dfs(end + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res

