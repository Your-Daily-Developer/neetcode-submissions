from typing import List
from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        @cache
        def dfs(i: int, j: int) -> int:
            best = 1
            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))
            return best
        
        return max(dfs(i, j) for i in range(m) for j in range(n))