class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]
        end = intervals[0][1]
        j = 0

        for i in range(1,len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1],end)
                res[j][1] = end
            else:
                res.append(intervals[i])
                end = intervals[i][1]
                j += 1
        
        return res

