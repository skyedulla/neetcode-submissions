class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        
        digit_store = []
        for item in tokens:
            
            if item in digits or len(item) > 1:
                digit_store.append(int(item))

            else:
                if item == '+':
                    ending_digit = digit_store.pop()
                    starting_digit = digit_store.pop()
                    digit_store.append(starting_digit + ending_digit)
                elif item == '-':
                    ending_digit = digit_store.pop()
                    starting_digit = digit_store.pop()
                    digit_store.append(starting_digit - ending_digit)
                elif item == '*':
                    ending_digit = digit_store.pop()
                    starting_digit = digit_store.pop()
                    digit_store.append(starting_digit * ending_digit)
                elif item == '/':
                    ending_digit = digit_store.pop()
                    starting_digit = digit_store.pop()
                    digit_store.append(int(starting_digit / ending_digit))
                    
                    

                    
        return digit_store[-1]
                
