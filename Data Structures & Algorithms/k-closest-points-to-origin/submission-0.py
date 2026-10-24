class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((point[0] - 0)**2 + (point[1] - 0)**2,i) for i,point in enumerate(points)]

        heapq.heapify(distances)

        res = []

        for j in range(k):
            res.append(points[heapq.heappop(distances)[1]])
        
        return res