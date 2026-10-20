class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bins = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num,f in freq.items():
            bins[f].append(num)

        i = len(bins) - 1
        while len(res) < k:
            for elem in bins[i]:
                if len(res) >= k:
                    break
                res.append(elem)
            i -= 1

        return res
