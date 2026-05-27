class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        
        def checkNeighbors(row, col, index, history):
            if index == len(word):
                return True
            if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
                return False
            if board[row][col] != word[index]:
                return False
            if (row, col) in history:
                return False
            
            history.append((row, col))
            
            if checkNeighbors(row - 1, col, index + 1, history) or checkNeighbors(row + 1, col, index + 1, history) or checkNeighbors(row, col - 1, index + 1, history) or checkNeighbors(row, col + 1, index + 1, history):
                return True
            
            history.pop()

        rows = 0
        for i in range(len(board)):
            rows += 1

        cols = 0
        for i in range(len(board[0])):
            cols += 1

        history = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if checkNeighbors(i, j, 0, history):
                    return True
                
        return False
        


        
        