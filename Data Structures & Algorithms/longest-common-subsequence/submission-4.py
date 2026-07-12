class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #when a match occurs at a certain index, every cell with a higher row or col
        #should increment by one

        #every grid represents whether the index's are similar at that index
        #when a match occurs at index i, j then all index's greater than [i + 1][j + 1]
        #should be incremented by one

        #each cell should inherit from the cell above and to the left of it

        
        



        dp = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]

        
        
               

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
            
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            

        return dp[len(text2)][len(text1)]





                
