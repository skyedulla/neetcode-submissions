class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            pointer = trie
            for char in word:
                if char not in pointer:
                    pointer[char] = {}
                pointer = pointer[char]
                
            
            pointer['*'] = True

        """while using the trie to search for words I have to constantly check for *
            then I have to create a branch that goes back to trie and a branch for
            every single other charcter key within that dictionary"""
        memo = {}
        def searchTrie(index):
            if index in memo:
                return memo[index]

            dict_branch = trie
            while index < len(s):
                if '*' in dict_branch:
                    if searchTrie(index) == True:
                        memo[index] = True
                        return True
                if s[index] in dict_branch:
                    dict_branch = dict_branch[s[index]]
                else:
                    memo[index] = False
                    return False
                    
                    
                index += 1

            if '*' in dict_branch:
                memo[index] = True
                return True
            else:
                memo[index] = False
                return False

            return memo[index]

        return searchTrie(0)

                