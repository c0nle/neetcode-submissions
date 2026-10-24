class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0

        def dfs(x,y):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                return 0
            elif grid[y][x] == 0:
                return 0
            else:
                grid[y][x] = 0
                return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)
        
        
        for y,row in enumerate(grid):
            for x,num in enumerate(row):
                res = max(res,dfs(x,y))
        
        return res