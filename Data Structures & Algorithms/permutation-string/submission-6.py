class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        repeats = []

        dynamic_list = []
        for letter in s1:
            dynamic_list.append(letter)

        for right in range(len(s2)):
            if s2[right] in s1: 
                if s2[right] in dynamic_list:
                    dynamic_list.remove(s2[right])
                else:
                    repeats.append(s2[right])
                    
            while right >= len(s1) + left:
                if s2[left] in s1:
                    if s2[left] in repeats:
                        repeats.remove(s2[left])
                    else:
                        dynamic_list.append(s2[left])

                left += 1 

            if dynamic_list == []:
                return True

        
        return False