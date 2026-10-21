class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            res = 0
            while n != 0:
                if n % 2 == 1: res += 1
                n = n // 2
            return res
        
        res = []
        
        for num in range(n+1):
            res.append(countOnes(num))
        
        return res
