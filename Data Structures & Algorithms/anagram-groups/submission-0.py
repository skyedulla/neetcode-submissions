class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
        
        answer = []
        for array in anagrams.values():
            answer.append(array)

        return answer