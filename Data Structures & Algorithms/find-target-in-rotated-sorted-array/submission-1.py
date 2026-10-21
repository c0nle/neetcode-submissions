class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r+l) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l

        l, r =  0, len(nums) - 1

        while l <= r:
            mid = (r+l) // 2
            index = (mid + pivot) % len(nums)
            if nums[index] == target:
                return index
            elif nums[index] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

            