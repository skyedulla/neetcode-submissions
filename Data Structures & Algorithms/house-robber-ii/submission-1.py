class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def chooseHouse(start, end):
            memo = {}
            def helper(index):
                if index in memo:
                    return memo[index]
                
                if index > end:
                    return 0
                
                choice1 = nums[index] + helper(index + 2)
                choice2 = 0
                if not index + 1 > end:
                    choice2 = nums[index + 1] + helper(index + 3)

                memo[index] = max(choice1, choice2)
                return memo[index]
            
            return helper(start)
        
        return max(chooseHouse(0, len(nums) - 2), chooseHouse(1, len(nums) - 1))
