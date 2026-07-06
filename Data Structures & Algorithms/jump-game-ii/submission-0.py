class Solution:
    def jump(self, nums: List[int]) -> int:

        end_of_jump = 0
        farthest = 0
        jumps = 0
        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == end_of_jump:
                jumps += 1
                end_of_jump = farthest

                
        return jumps


                







