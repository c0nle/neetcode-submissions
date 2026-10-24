"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = Node(node.val,node.neighbors)
        visit = deque([start])
        res = {}
        res[start] = Node(node.val)

        def bfs(cur):
            while visit:
                cur = visit.popleft()
                for neighbor in cur.neighbors:
                    if neighbor not in res:
                        res[neighbor] = Node(neighbor.val)
                        visit.append(neighbor)
                    res[cur].neighbors.append(res[neighbor])

        bfs(start)
        return res[start]