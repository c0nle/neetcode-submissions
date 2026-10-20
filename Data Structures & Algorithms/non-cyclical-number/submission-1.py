class Solution:
    def isHappy(self, n: int) -> bool:
        cur = str(n)
        visited = set()
        while cur not in visited:
            helper = 0
            visited.add(cur)
            for num in cur:
                helper += pow(int(num),2)
            cur = str(helper)
            if cur == "1":
                return True

        return False
