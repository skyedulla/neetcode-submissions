class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append(i)

        return result
        

        #if the stack is empty we simply append the index to the stack
        #(ex: when the algorithm starts the stack is empty append 0)

        #if the stack isn't empty compare the current_index temp to the last 
        #index in the stack's temp. If the curr_temp is warmer remove
        #that item from the stack and find the difference of days.
        #repeat this process of checking the current day against the last
        #day until the stack is emptry or the current temperature is not 
        #greater.

        #then append the index to the temp. This creates a monotonic decreasing
        #array. Elements left on the stack at the end of the program are days
        #that have never experience a future warmer day. These values are already
        #defaulted to 0. 
