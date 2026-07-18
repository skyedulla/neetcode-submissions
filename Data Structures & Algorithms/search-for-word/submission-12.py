class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def valid_coor(row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            else:
                return True

        def checkNeighbors(row, col, word_index, path):
            if word_index == len(word):
                return True
            if not valid_coor(row, col):
                return
            if board[row][col] != word[word_index]:
                return

            path.add((row, col))
            for dr, dc in directions:
                row += dr
                col += dc
                if (row, col) not in path:
                    if checkNeighbors(row, col, word_index + 1, path):
                        return True
                row -= dr
                col -= dc
            
            path.remove((row, col))

                



        for i in range(len(board)):
            for j in range(len(board[0])):
                if checkNeighbors(i, j, 0, set()):
                    return True

        return False