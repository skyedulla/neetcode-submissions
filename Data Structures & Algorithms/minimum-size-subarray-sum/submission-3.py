class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        """the input constraints is 100,000 meaning we need O(nlogn) or better. The proposed
        formula is O(n+k) since we are splicing the list and calculating sum.
        
        I'll update the algorithm by maintaining a sum variable. When I move pointers.
        when sum < target: right + 1
        when sum becomes greater than target. calculate the total length
        when sum > target: check if right - left + 1 > max_length
        This will be O(2n) at the worst case which should pass easily with an input of 100,000 """


        left = 0
        right = 0
        sum = nums[0]
        min_length = float('inf')
        while right < len(nums) and left < len(nums):
            if sum < target:
                right += 1
                if right >= len(nums):
                    break
                sum += nums[right]
            
            elif sum >= target:
                min_length = min(right - left + 1, min_length)

                sum -= nums[left]
                left += 1

        
        
        if min_length == float('inf'):
            return 0
        else:
            return min_length


            