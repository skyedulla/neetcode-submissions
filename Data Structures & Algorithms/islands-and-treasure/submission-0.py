class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def dfs(row, col, distance):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if distance != 0:
                if grid[row][col] < distance:
                    return
            
            grid[row][col] = min(grid[row][col], distance)
            
            distance += 1
            dfs(row + 1, col, distance)
            dfs(row - 1, col, distance)
            dfs(row, col + 1, distance)
            dfs(row, col - 1, distance)
            distance -= 1

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)