class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        treasures = deque()
        
        water, treasure, land = -1, 0, 2147483647

        def addCell(x,y):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or (x,y) in visited or grid[y][x] == -1:
                return
            treasures.append([x,y])
            visited.add((x,y))

        for y,row in enumerate(grid):
            for x,num in enumerate(row):
                if num == treasure:
                    treasures.append([x,y])
                    visited.add((x,y))
        
        dist = 0
        while treasures:
            for i in range(len(treasures)):
                x,y = treasures.popleft()
                grid[y][x] = dist
                addCell(x+1,y)
                addCell(x-1,y)
                addCell(x,y+1)
                addCell(x,y-1)
            dist += 1
