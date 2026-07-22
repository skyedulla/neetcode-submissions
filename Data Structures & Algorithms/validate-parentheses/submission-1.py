class Solution:
    def isValid(self, s: str) -> bool:
        #the brackets need to be closed in a particular order
        #the order changes depending on the most recent opening bracket

        #We'll append items to a stack 
        
        #We'll classify items as opening and closing 

        #opening brackets are always valid
        
        #closing brackets must be the closing brackets of the
        #opening bracket in the stack

        #we'll directly appending closing brackets onto the stack
        #so that we can make comparisons directly

        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(')')
            elif bracket == '{':
                stack.append('}')
            elif bracket == '[':
                stack.append(']')
            else:
                if stack == []:
                    return False

                required_bracket = stack.pop()
                if bracket != required_bracket:
                    return False

        #we check to ensure there aren't any unclosed brackets in the string
        if stack == []:
            return True
        else:
            return False


            
