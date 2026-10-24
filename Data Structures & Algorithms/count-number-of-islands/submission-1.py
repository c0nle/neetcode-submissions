class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        
        def dfs(x,y):
            if x >= len(grid[0]) or x < 0 or y >= len(grid) or y < 0:
                return
            if grid[y][x] == "0":
                return
            elif grid[y][x] == "1":
                grid[y][x] = "0"
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
        

        for y,row in enumerate(grid):
            for x,num in enumerate(row):
                if num == "1":
                    res += 1
                    dfs(x,y)
        
        return res