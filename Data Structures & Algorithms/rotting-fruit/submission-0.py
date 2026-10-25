class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rottenFruits = deque()

        def addFruit(x,y):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or (x,y) in visited or grid[y][x] == 0:
                return
            rottenFruits.append([x,y])
            visited.add((x,y))

        for y,row in enumerate(grid):
            for x,num in enumerate(row):
                if num == 2:
                    rottenFruits.append([x,y])
                    visited.add((x,y))
        
        time = 0
        while rottenFruits:
            for i in range(len(rottenFruits)):
                x,y = rottenFruits.popleft()
                grid[y][x] = 2
                addFruit(x+1,y)
                addFruit(x-1,y)
                addFruit(x,y+1)
                addFruit(x,y-1)
            time += 1
        
        for row in grid:
            for num in row:
                if num == 1:
                    return -1
        
        return max(0,time-1)