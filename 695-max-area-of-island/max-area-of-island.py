class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        visited = set()

        def dfs(r, c): 
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1: 
                return 0 
            if (r, c) in visited or grid[r][c] == 0: 
                return 0 

            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1) + dfs(r - 1, c)


        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                # if (i, j) not in visited and grid[i][j] == 1: 
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
        