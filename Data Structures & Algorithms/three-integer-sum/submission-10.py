class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        #the loop should iterate for the first number in the list regardless of 
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if nums[i] == nums[i - 1] and i > 0:
                continue
            
        
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    if [nums[i], nums[left], nums[right]] not in output:
                        output.append([nums[i], nums[left], nums[right]])
                    left += 1
            
        return output