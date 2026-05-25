class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_map = {}
        highest_range = 0
        highest_freq = 0
        
        #updates the char_map dictionary and returns the highest_frequency of a character
        def updateMap(char_map, character, increment):
            if increment:
                if character in char_map:
                    char_map[character] += 1
                else:
                    char_map[character] = 1
            else:
                char_map[character] -= 1

            highest_freq = 0
            for value in char_map.values():
                if value > highest_freq:
                    highest_freq = value

            return highest_freq
            


        #starting at right = 0 we increment right until right reaches the last char in s
        for right in range(len(s)):
            #we add the new char to the char_map and we return the highest frequency of a character within the current range
            highest_freq = updateMap(char_map, s[right], True)

            #we calculate the numbers of chars that need to be replace within the current range from left to right
            #if right = 0 and left = 0, the number of chars to replace = 0, 
            #if right = 1 and left = 0 the number of chars to replace is 2 - highest_freq which is either 1 or 2 since the range has 2 letters. 
            #the chars_to_replace condition is met only if the highest_freq is 2 which means the chars are the same which will cause the while loop condition to not be meant, updating highest_range to two and increasing the right pointer, recalculating highest_freq and chars_to_replace to see if the condition is met again
            chars_to_replace = (right - left + 1) - highest_freq

            #we ensure that the number of chars_to_replace isn't greater than k before calculating highest range to ensure that the condition is met
            while chars_to_replace > k:
                highest_freq = updateMap(char_map, s[left], False)
                left += 1
                #we recalculate chars to replace inside of the while loop after updating highest_frequency and moving the left pointer. if it isn't recalculated then it will get stuck in an endless loop
                chars_to_replace = (right - left + 1) - highest_freq

            #we calculate the current range and we update highest range if the current range is greater than the previous highest range
            highest_range = max(highest_range, right - left + 1)


        return highest_range
            

        