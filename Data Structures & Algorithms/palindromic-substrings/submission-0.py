class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def checkNeighbors(index1, index2):
            if index1 < 0:
                return 0
            if index2 > len(s) - 1:
                return 0

            if s[index1] == s[index2]:
                return 1 + checkNeighbors(index1 - 1, index2 + 1)
            else:
                return 0

        #every index should call checkNeighbors , index and index + 1

        substring_count = len(s)
        substring_count += checkNeighbors(0, 1)

        for index in range(1, len(s) - 1):
            substring_count += checkNeighbors(index - 1, index + 1)
            substring_count += checkNeighbors(index, index + 1)
        
        return substring_count
