"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i:i.start)

        if not intervals: return 0

        heap = [intervals[0].end]

        for interval in intervals[1:]:
            if interval.start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,interval.end)

        return len(heap)