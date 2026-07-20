class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Performing dfs would allow us to fully count the nodes of an island from
        #the first branch. 

        #While checking each node I will add it to a visited array. This way we
        #don't initiated the function on land that was already checked'



        def dfs(row, col):
            if min(row, col) < 0 or col >= len(grid[0]) or row >= len(grid):
                return 0 
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0 
            #we turn the land into a 0 so it can no longer get detected as
            #this ensures that the total number of lands detected will always
            #be equal to the number of 1's
            
            island_size = 1
            island_size += dfs(row + 1, col)
            island_size += dfs(row - 1, col)
            island_size += dfs(row, col + 1)
            island_size += dfs(row, col - 1)
        
            return island_size

            

        max_island_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    island_size = dfs(i, j)

                    if island_size >= max_island_size:
                        max_island_size = island_size



        return max_island_size

