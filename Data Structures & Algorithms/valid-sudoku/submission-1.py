from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def identifyBox(row, col):
            if row <= 2:
                if col <= 2:
                    return 0
                elif col <= 5:
                    return 1
                elif col <= 8:
                    return 2
            elif row <= 5:
                if col <= 2:
                    return 3
                elif col <= 5:
                    return 4
                elif col <= 8:
                    return 5
            elif row <= 8:
                if col <= 2:
                    return 6
                elif col <= 5:
                    return 7
                elif col <= 8:
                    return 8


        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
                

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    value = board[i][j]
                    row = i
                    col = j
                    box = identifyBox(i, j)
                    if value in rows[row]:
                        return False
                    if value in cols[col]:
                        return False
                    if value in boxes[box]:
                        return False

                    rows[row].add(value)
                    cols[col].add(value)
                    boxes[box].add(value)
                    
        return True




        
                    
