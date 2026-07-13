class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #This program will be 2^n with 20 inputs which is an adequate time complexity.
        """we will explore every combination of choices by adding and subtracting at
        each utilizing recursion."""

        nums_total_sum = sum(nums)
        zero_sums = 0
        def branch(index, curr_total):
            if curr_total < target:
                return 0

            if index == len(nums):
                if curr_total == target:
                    return 1
                return 0
            
            return branch(index + 1, curr_total - (2 * nums[index])) + branch(index + 1, curr_total)
        
        return branch(0, nums_total_sum)

        

        # with an input of 20 this will run 2^20 times. It will always run 2^n times

        
        
                    
