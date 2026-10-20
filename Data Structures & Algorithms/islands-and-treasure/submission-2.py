class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(x,y):
            q = deque()
            visited = set()
            q.append((x, y, 0))          # (x, y, dist)
            visited.add((x, y))

            while q:
                cx, cy, dist = q.popleft()

                if grid[cy][cx] == 0:
                    return dist

                if grid[cy][cx] != -1:   # keine Wand
                    if cx < cols - 1 and (cx + 1, cy) not in visited and grid[cy][cx + 1] != -1:
                        visited.add((cx + 1, cy))
                        q.append((cx + 1, cy, dist + 1))
                    if cx > 0 and (cx - 1, cy) not in visited and grid[cy][cx - 1] != -1:
                        visited.add((cx - 1, cy))
                        q.append((cx - 1, cy, dist + 1))
                    if cy < rows - 1 and (cx, cy + 1) not in visited and grid[cy + 1][cx] != -1:
                        visited.add((cx, cy + 1))
                        q.append((cx, cy + 1, dist + 1))
                    if cy > 0 and (cx, cy - 1) not in visited and grid[cy - 1][cx] != -1:
                        visited.add((cx, cy - 1))
                        q.append((cx, cy - 1, dist + 1))

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == INF:
                    grid[y][x] = bfs(x,y)
        
