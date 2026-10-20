class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = dict()
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros[i] = 1

        if len(zeros) > 1:
            return res

        for i in range(len(nums)):
            if i in zeros:
                res[i] = product
            elif len(zeros) > 0:
                res[i] = 0
            else:
                res[i] = product//nums[i]

        return res