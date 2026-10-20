class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i<j:
            summe = numbers[i] + numbers[j]
            if summe > target:
                j -= 1
            elif summe < target:
                i += 1
            else:
                return [i+1,j+1]