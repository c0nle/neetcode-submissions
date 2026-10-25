class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start,end in intervals:
            lastStart, lastEnd = res.pop()
            if start <= lastEnd:
                newEnd = max(end,lastEnd)
                res.append([lastStart,newEnd])
            else:
                res.append([lastStart,lastEnd])
                res.append([start,end])
        
        return res