class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def copyConfiguration(path, array):
            configuration = []

            index = 0
            lastQueenMarked = False
            for i in range(n):
                string = ""
                for j in range(n):
                    if lastQueenMarked == False and (i, j) == path[index]:
                        string += 'Q'
                        index += 1
                        if index == len(path):
                            lastQueenMarked = True
                    else:
                        string += '.'
                
                configuration.append(string)
            
            array.append(configuration)


        cols_taken = [False] * n
        left_diagonals = set()
        right_diagonals = set()

        valid_configurations = []

        def computePossibilities(row, path):
            if row == n:
                copyConfiguration(path, valid_configurations)
                return
        

            for i in range(n):
                if (
                    cols_taken[i] == False 
                    and (row - i) not in left_diagonals 
                    and (row + i) not in right_diagonals
                ):
                
                    path.append((row, i))
                    cols_taken[i] = True
                    left_diagonals.add(row - i)
                    right_diagonals.add(row + i)
                    computePossibilities(row + 1, path)
                    left_diagonals.remove(row - i)
                    right_diagonals.remove(row + i)
                    cols_taken[i] = False
                    path.pop()

        
        
        computePossibilities(0, [])
        return valid_configurations
        
