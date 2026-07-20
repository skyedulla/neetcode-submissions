class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """this problem can be solved incrementally with bfs by adding all rotten oranges to
        a starting queue. Then we will call a for loop popping the row, col from the queue
        and convert all 4 adjacent cells to rotten oranges if they are not already rotten.
        We will count the number of converted oranges.
        We will create an inital count of oranges and perform an adjacent search on all fresh'
        oranges to check if they can become rotted. If one of them can't then we will return -1.
        """

        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()

        minutes = 0
        fresh_fruit_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_fruit_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    


        minutes = 0
        while queue and fresh_fruit_count != 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in DIRECTIONS:
                    n_row = row + dr
                    n_col = col + dc

                    if min(n_row, n_col) < 0 or n_row >= len(grid) or n_col >= len(grid[0]):
                        continue
                    if grid[n_row][n_col] == 0 or grid[n_row][n_col] == 2:
                        continue

                    fresh_fruit_count -= 1
                    grid[n_row][n_col] = 2
                    queue.append((n_row, n_col))
                        
            minutes += 1

        #if there is 0 fresh fruit then I shouldn't wait for loop to elapse unessarily
        if fresh_fruit_count > 0:
            return - 1
        else:
            return minutes

        

