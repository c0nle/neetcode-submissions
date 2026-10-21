class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        div = n
        while div != 0:
            if div % 2 == 1:
                res += 1
            div = div // 2

        return res
    