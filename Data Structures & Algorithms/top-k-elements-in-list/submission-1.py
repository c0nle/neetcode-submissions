class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key,value in count.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
