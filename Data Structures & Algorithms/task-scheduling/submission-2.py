import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-c for c in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()                          # [restCount (negativ), wieder verfügbar ab]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1     # ausführen: ein Vorkommen weniger
                if cnt:                              # noch Vorkommen übrig?
                    q.append([cnt, time + n])        # in den Cooldown
            # sonst: Leerlauf in diesem Schritt

            if q and q[0][1] == time:                # Cooldown abgelaufen?
                heapq.heappush(maxHeap, q.popleft()[0])

        return time