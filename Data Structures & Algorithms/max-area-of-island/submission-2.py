class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width,height = len(grid[0]), len(grid)
        res = 0
        visited = set()
    
        def dfs(x,y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == 0 or (x,y) in visited:
                return 0
            else:
                visited.add((x,y))
                return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)

        for x in range(width):
            for y in range(height):
                if grid[y][x] == 1:
                    res = max(res,dfs(x,y))
        return res