class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = sorted(Counter(tasks).values(), reverse=True)
        maxCount = counts[0]
        idle = (maxCount - 1) * n                  

        for c in counts[1:]:
            idle -= min(c, maxCount - 1)           

        return len(tasks) + max(idle, 0)