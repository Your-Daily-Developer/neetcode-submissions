class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 0):
                return 0
            
            # Mark as visited
            grid[r][c] = 0
            
            # Count current cell + explore 4 directions
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area