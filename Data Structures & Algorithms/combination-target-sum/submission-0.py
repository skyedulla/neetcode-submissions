class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #since we can choose the same number an infinite amount of time
        #we need to setup our recursive calls to loop through the entire
        #array while tracking a sum variable.

        #we use the sum variable to determine when to backtrack (i.e if sum > target)
        
        valid_combinations = []

        def checkCombinations(curr_comb, starting_index):
            if sum(curr_comb) > target:
                return
            elif sum(curr_comb) == target:
                valid_combinations.append(list(curr_comb))
                return 

            #tracking the loops we completed ensures that we don't repeatedly try the same combinations
            #the way the call stack unwinds otherwise is 2 2 2 2 2 5 then when we get back 
            #to here 2 2 it will got 2 5 2 2 2 2 2 2. Instead we pass loops_completed as 1. and it will
            #now try 2 5 5 5 5 5 for the first combination. After we complete all combinations that
            #include a 2 we never try to again since the main loop is now always passing in a starting
            #index with 1 or greater.

            loops_completed = starting_index
            for i in range(starting_index, len(nums)):
                curr_comb.append(nums[i])
                checkCombinations(curr_comb, loops_completed)
                curr_comb.pop()
                loops_completed += 1

        checkCombinations([], 0)
        return valid_combinations