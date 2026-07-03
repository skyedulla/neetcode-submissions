
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)


        def addSum(curr_sum, i):
            if i > len(nums) - 1:
                return False
            if curr_sum > total_sum / 2:
                return False
            if curr_sum == total_sum / 2:
                return True

            if addSum(curr_sum + nums[i], i + 1):
                return True
            if addSum(curr_sum, i + 1):
                return True

            
            return False

        return addSum(0, 0)
            








