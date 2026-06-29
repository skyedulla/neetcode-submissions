class Solution:
    def canJump(self, nums: List[int]) -> bool:

        current_index = len(nums) - 1 #this is the last index
        distance_required = 0 #initialize the distance required to zero
        while current_index > 0:
            current_index -= 1 # move down an index
            distance_required += 1 #move the distance required up with the move in index

            if nums[current_index] >= distance_required:
                distance_required = 0 # if the value of the jump in a current index is higher or equal to the distance required than that index has a route to the end so reset the distance required to zero since the jump only needs to reach the current_index to be true
        
        
        if distance_required == 0:
            return True
        else:
            return False
            
        
