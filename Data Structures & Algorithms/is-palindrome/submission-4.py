class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i]
                
        
        string = string.lower()

        if string == string[::-1]:
            return True
        else:
            return False
        