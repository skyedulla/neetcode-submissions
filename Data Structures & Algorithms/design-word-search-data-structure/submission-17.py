class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
            
    
            
    def search(self, word: str) -> bool:
       
        def dfs(index, search_node):
            if index == len(word) and search_node.is_end:
                return True
            if index == len(word) and not search_node.is_end:
                return False
    
            if word[index] == '.':
                for char, node in search_node.children.items():
                    if dfs(index + 1, node):
                        return True

            if word[index] in search_node.children:
                return dfs(index + 1, search_node.children[word[index]])

            return False


        root = self.root 
        if dfs(0, root):
            return True
        else:
            return False
            
                

        
        
