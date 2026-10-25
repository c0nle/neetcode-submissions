class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart,newEnd = newInterval[0], newInterval[1]
        for i, (start,end) in enumerate(intervals):
            if start > newEnd:
                res.append([newStart,newEnd])
                return res + intervals[i:]
            elif newStart <= end:
                newStart = min(start,newStart)
                newEnd = max(end,newEnd)
            else:
                res.append([start,end])

        res.append([newStart,newEnd])

        return res