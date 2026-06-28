class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_sum = nums[0]
        index_range = (0, 0)
        running_sum = 0
        while right < len(nums):
            running_sum += nums[right]

            if running_sum > max_sum:
                index_range = (left, right)
                max_sum = running_sum

            if running_sum < 0:
                left = right + 1
                running_sum = 0

            

            
            right += 1
        
        

        return max_sum



        