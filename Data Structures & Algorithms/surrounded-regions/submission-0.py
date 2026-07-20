class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        """
        We have two options:

        One involves running a dfs algorithm on all of the bordering cells
        on the board and converting O's to E's. 
        Then we run a full iteration through the board. Turning O's to X's and
        E's to O's 

        The second approach involves using dfs on every single O on the board
        and then converting the O to an X if all of the recursive calls return
        a value of 1. The default return value is one and the conditional return
        value is 0 which occurs when a branch tries to recursively call on a non
        existing cell. This approach would only require recursively calling O's.


        The first algorithm is much simpler to understand and perform. Both algorithms
        have similar time complexities and space complexities. Therefore, I will
        implement the first algorithm.
        """


        def dfs(row, col):
            if min(row, col) < 0 or row >= len(board) or col >= len(board[0]):
                return
            if board[row][col] == 'X' or board[row][col] == 'E':
                return 
            
            board[row][col] = 'E'

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    dfs(i, j)

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'E':
                    board[i][j] = 'O'


