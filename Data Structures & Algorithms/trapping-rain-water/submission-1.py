from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:
        total_trap = 0

        left = 0
        leftMax = 0
        right = len(height) - 1
        rightMax = len(height) - 1

        while left < right:
            
            if height[leftMax] > height[rightMax]:

                if height[right] > height[rightMax]:
                    rightMax = right  
                else:
                    right -= 1
                    trapped_water = height[rightMax] - height[right]
                    

            else:

                if height[left] > height[leftMax]:
                    leftMax = left
                else:
                    left += 1
                    trapped_water = height[leftMax] - height[left]
            
            if trapped_water > 0:
                total_trap += trapped_water

        return total_trap
                    
                
            
        

        

                

                    
                


            