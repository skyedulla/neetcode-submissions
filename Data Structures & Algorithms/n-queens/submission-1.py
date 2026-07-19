class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def findPlacement(board, coordinate):
            if coordinate[0] >= len(board) or coordinate[1] >= len(board[0]):
                return None

            row, col = coordinate
            for j in range(col, len(board[0])):
                if board[row][j] == 0:
                    return (row, j)

            for i in range(row + 1, len(board)):
                for j in range(0, len(board[0])):
                    if board[i][j] == 0:
                        return (i, j)

            return None

       
        def updateGrid(board, coordinate, add):
            row, col = coordinate
            
            if add:
                d = 1
            else:
                d = -1

            for i in range(0, len(board)):
                board[i][col] += d
            for j in range(0, len(board)):
                board[row][j] += d
            board[row][col] -= d

            i = 1
            boundary_reached = False
            while boundary_reached == False:
                boundary_reached = True
                if row + i < n and col + i < n:
                    board[row + i][col + i] += d
                    boundary_reached = False

                if row + i < n and col - i >= 0:
                    board[row + i][col - i] += d
                    boundary_reached = False

                if row - i >= 0 and col + i < n:
                    board[row - i][col + i] += d
                    boundary_reached = False

                if row - i >= 0 and col - i >= 0:
                    board[row - i][col - i] += d
                    boundary_reached = False
                
                i += 1




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




        valid_configurations = []
        def computePossibilities(board, path):
            if len(path) == n:
                copyConfiguration(path, valid_configurations)
                return
            
            
            if path == []:
                next_valid_coordinate = (0, 0)
            else:
                if path[-1][1] + 1 < n:
                    next_valid_coordinate = (path[-1][0], path[-1][1] + 1)
                else:
                    next_valid_coordinate = (path[-1][0] + 1, 0)
            

            while True:
                coordinate = findPlacement(board, next_valid_coordinate)
                if coordinate == None:
                    return 
                
                path.append(coordinate)
                updateGrid(board, coordinate, True)
                computePossibilities(board, path)
                updateGrid(board, coordinate, False)
                path.pop()

                if coordinate[1] + 1 < n:
                    next_valid_coordinate = (coordinate[0], coordinate[1] + 1)
                else:
                    next_valid_coordinate = (coordinate[0] + 1, 0)
        
        board = [[0] * n for i in range(n)]
        computePossibilities(board, [])
        return valid_configurations
        
