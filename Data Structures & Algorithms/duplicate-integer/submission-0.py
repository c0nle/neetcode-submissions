class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for i in nums:
            if i in values:
                return True
            else:
                values.add(i)
        return False