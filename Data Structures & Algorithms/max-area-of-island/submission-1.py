class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width,height = len(grid[0]), len(grid)
        res = 0
        for x in range(width):
            for y in range(height):
                if grid[y][x] == 1:
                    res = max(res,self.dfs(x,y,grid))
        return res
    
    def dfs(self,x,y,grid):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == 0:
            return 0
        else:
            grid[y][x] = 0
            return 1 + self.dfs(x+1,y,grid) + self.dfs(x-1,y,grid) + self.dfs(x,y+1,grid) + self.dfs(x,y-1,grid)
