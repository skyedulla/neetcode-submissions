from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashmap = defaultdict(list)
        for i in range(len(wordList)):
            convert = list(wordList[i])
            for j in range(len(wordList[i])):
                char = convert[j]
                convert[j] = '*'
                hashmap[str(convert)].append(wordList[i])
                convert[j] = char
                
            
        

        
    
        
        queue = deque([beginWord])
        transforms = 1
        visited = {beginWord}
        while queue:
            for i in range(len(queue)):
                query = queue.popleft()
                
                
                convert = list(query)
                for j in range(len(query)):
                    char = convert[j]
                    convert[j] = '*'

                    if str(convert) in hashmap:
                        for word in hashmap[str(convert)]:
                            if word == endWord:
                                return transforms + 1
                            if word not in visited:
                                visited.add(word)
                                queue.append(word)
                            

                    convert[j] = char
                

            transforms += 1
            
        return 0
