class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rottenFruits = deque()
        fresh = 0

        def addFruit(x,y):
            nonlocal fresh
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or (x,y) in visited or grid[y][x] == 0:
                return
            rottenFruits.append([x,y])
            visited.add((x,y))
            fresh -= 1

        for y,row in enumerate(grid):
            for x,num in enumerate(row):
                if num == 2:
                    rottenFruits.append([x,y])
                    visited.add((x,y))
                elif num == 1:
                    fresh += 1
        
        time = 0
        while rottenFruits and fresh > 0:
            for i in range(len(rottenFruits)):
                x,y = rottenFruits.popleft()
                grid[y][x] = 2
                addFruit(x+1,y)
                addFruit(x-1,y)
                addFruit(x,y+1)
                addFruit(x,y-1)
            time += 1
        
        return time if fresh == 0 else -1