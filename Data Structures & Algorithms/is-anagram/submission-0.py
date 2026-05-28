class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if we create a dictionary of frequencies in s then we can substract the values when checking t and if all values in the dict = 0 then return true
        #this is much more efficient then a list because the character search will be O(1) compared to potentially O(n) for lists and we use less memory if we use a dictionary for longer strings

        char_frequency = {}

        for letter in s:
            if letter in char_frequency:
                char_frequency[letter] += 1
            else:
                char_frequency[letter] = 1

        for letter in t:
            if letter in char_frequency:
                char_frequency[letter] -= 1
            else:
                return False

        for value in char_frequency.values():
            if value != 0:
                return False
        return True