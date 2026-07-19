class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Create a trie of the input words list

        #create a backtracking algorithm that has a visited coordinate set

        #when backtrack is called on a cell it queries the trie to check if a value exists

        #since each square contains a single character, the trie will use O(1) search
        #there is no need to backtrack if a branch doesn't find any matches.
        #if a match is made the search ptr advances through the trie. At each level the algorithm
        #checks for '*'. and saves the current word to res and continutes
        trie = {}
        for word in words:
            ptr = trie
            for char in word:
                if char not in ptr:
                    ptr[char] = {}
                ptr = ptr[char]
            ptr['*'] = {}

        
        visited = set()
        def checkBlock(row, col, search_node, visited, word):
            if '*' in search_node:
                w = "".join(word)
                res.add(w)
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            if (row, col) in visited:
                return

            letter = board[row][col] 
            if letter not in search_node:
                return
            
            
            visited.add((row, col))
            word.append(letter)
            checkBlock(row + 1, col, search_node[letter], visited, word)
            checkBlock(row - 1, col, search_node[letter], visited, word)
            checkBlock(row, col + 1, search_node[letter], visited, word)
            checkBlock(row, col - 1, search_node[letter], visited, word)
            word.pop()
            visited.remove((row, col))
            
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                checkBlock(i, j, trie, visited, [])
        
        return list(res)


