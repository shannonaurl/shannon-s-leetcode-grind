class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0 

        def dfs(r, c): 
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1: 
                return True 
            
            if grid[r][c] == "0" or (r, c) in visited: 
                return True 
        
            visited.add((r, c))
            return dfs(r+1, c) and dfs(r, c+1) and dfs(r-1, c) and dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                if (r, c) in visited: 
                    continue 
                if grid[r][c] == "1": 
                    if dfs(r, c) == True: 
                        count += 1 
        
        return count 



                

        