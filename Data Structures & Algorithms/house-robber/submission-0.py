class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        if n == 3: return max(nums[0] + nums[2], nums[1])

        last_house = max(nums[0], nums[1])
        curr_house = nums[0] + nums[2]

        for i in range(3, len(nums)):
            next_house = max(curr_house, nums[i] + last_house)

            last_robbed_house = last_house
            last_house = curr_house
            curr_house = next_house
        
        return curr_house