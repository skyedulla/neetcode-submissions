class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        char_freqs = {}
        indicator = 0
        for char in t:
            if char in char_freqs:
                char_freqs[char] += 1
            else:
                char_freqs[char] = 1
                indicator += 1


        left = 0
        right = 0
        min_string = ""
        while True:
            if indicator > 0:
                if right >= len(s):
                    break

                if s[right] in char_freqs:
                    char_freqs[s[right]] -= 1
                    if char_freqs[s[right]] == 0:
                        indicator -= 1

                right += 1
            
            if indicator == 0:
                if min_string == "" or len(s[left:right]) < len(min_string):
                    min_string = s[left:right]

                if s[left] in char_freqs:
                    char_freqs[s[left]] += 1
                    if char_freqs[s[left]] == 1:
                        indicator += 1
                    

                left += 1
                
        return min_string

        
        

        """iterate through s while subtracting from the frequency list.
        while iterating through s, check if s[right] is in char_freqs. If yes do char_freqs[s[right]] -= 1
        everytime a decrement is made to char_freqs. If the decrement leads to 0 we reduce indicator by 1.
        everytime a increment is made to char_freqs. If the increment leads to 1 we increase indicator by 1.
        If indicator reaches 0, then s currently contains all chars in t.
        While all frequencies stay under or equal to 0 move left += 1. 
        The moment a frequency becomes higher then 0. take a snapshot of s[left - 1: right + 1]
        
        The time complexity for this is O(n)"""
