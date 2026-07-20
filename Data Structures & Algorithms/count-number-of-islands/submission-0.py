class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #If we use dfs then we can scan the entire grid for connecting land
        #from a single grid. We can then mark all those pieces of land and increment
        #the islands count by 1. 

        #We recursively call the algorithm on each (row, col) coordinate and if it is
        #already on marked land we prune it. 

        #The iteration of islands occurs only once directly when new land is detected
        #then the algorithm searches adjacent lands to mark them in the set.

        #We can lower the amount of recursive calls by utilizing forward checking
        #and also marking water cells as visited since marked land and water cells 
        #should both be pruned.

        def in_bounds(row, col):
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            else:
                return True

        
        def searchGrid(row, col, original):
            nonlocal islands
            if (row, col) in visited:
                return
            visited.add((row, col))
            if grid[row][col] == '0':
                return

            if original:
                islands += 1

            if (row + 1, col) not in visited and in_bounds(row + 1, col):
                searchGrid(row + 1, col, False)
            
            if (row - 1, col) not in visited and in_bounds(row - 1, col):
                searchGrid(row - 1, col, False)

            if (row, col + 1) not in visited and  in_bounds(row, col + 1):
                searchGrid(row, col + 1, False)

            if (row, col - 1) not in visited and in_bounds(row, col - 1):
                searchGrid(row, col - 1, False)

        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                searchGrid(i, j, True)

        return islands

