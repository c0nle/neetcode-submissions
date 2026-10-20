class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            h = self.countOnes(i)
            res.append(h)
        return res
    def countOnes(self,i: int) -> int:
        res = 0
        for j in range(32):
            if (1<<j) & i:
                res += 1
        return res