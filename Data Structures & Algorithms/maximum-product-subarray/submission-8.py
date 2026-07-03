class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_state = [0] * len(nums)
        second_state = [0] * len(nums)

        
        max_product = nums[0]
        

        for i in range(0, len(nums)):
            if first_state[i - 1] == 0 or i == 0:
                #reset program
                negative_occured = False
                first_state[i] = nums[i]
            else:
                #continue multiplying first_state
                first_state[i] = first_state[i - 1] * nums[i]
                
                #check to see if the condition for starting or multiplying second state occured
                if negative_occured: 
                    if second_state[i - 1] == 0: 
                        second_state[i] = nums[i]
                    else: 
                        second_state[i] = second_state[i - 1] * nums[i]

            if negative_occured:
                curr_max = max(first_state[i], second_state[i])
            else:
                curr_max = first_state[i]
            
            if curr_max > max_product:
                max_product = curr_max

            if nums[i] < 0:
                negative_occured = True
            
        return max_product

        


           
            
            

        

        

        