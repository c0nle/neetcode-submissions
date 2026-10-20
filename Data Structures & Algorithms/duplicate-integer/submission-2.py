class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for num in nums:
            hset.add(num)
        return not (len(hset) == len(nums))
