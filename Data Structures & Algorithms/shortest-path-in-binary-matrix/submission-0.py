from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
       
            

        queue = deque([(0, 0, 1)])
        
        DIRECTIONS = [
            (-1, 1 ), (0, 1 ), ( 1, 1),
            (-1, 0 ),          ( 1, 0),
            (-1, -1), (0, -1), (1, -1)
            ]
        while queue:
            row, col, length = queue.popleft()
            

            for dr, dc in DIRECTIONS:
                next_row = row + dr
                next_col = col + dc

                if min(next_row, next_col) < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                    continue
                if grid[next_row][next_col] == 1:
                    continue

                if next_row == len(grid) - 1 and next_col == len(grid[0]) - 1:
                    return length + 1

                queue.append((next_row, next_col, length + 1))
                grid[next_row][next_col] = 1

            
        return -1