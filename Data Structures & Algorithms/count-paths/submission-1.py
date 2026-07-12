class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """The number of paths to arrive at a certain square is equal to 
        the number of paths for the square to the right + the number of paths
        for the square above"""

        dp = [[0] * n for i in range(m)]

        for row in range(0, m):
            dp[row][0] = 1
        
        for col in range(1, n):
            dp[0][col] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        

        return dp[m - 1][n - 1]
        
