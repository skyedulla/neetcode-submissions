class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def choice(index, j):
            if (index, j) in memo:
                return memo[index, j]

            if index == len(nums):
                return 0

            res = choice(index + 1, j)

            if j == -1 or nums[index] > nums[j]:
                res = max(1 + choice(index + 1, index), choice(index + 1, j))
            
                
            memo[index, j] = res
            return memo[index, j]
            
        return choice(0, -1)



                


                

            
            