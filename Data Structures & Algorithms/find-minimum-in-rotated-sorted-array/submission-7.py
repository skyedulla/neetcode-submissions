class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[0] < nums[-1]:
            return nums[0]
        #when left is right - 1 end the loop 
        while  right > left + 1:
            midpoint = left + ((right - left) // 2)

            if nums[left] < nums[midpoint]:
                left = midpoint
            else:
                right = midpoint

        return nums[right]

            
            
        
