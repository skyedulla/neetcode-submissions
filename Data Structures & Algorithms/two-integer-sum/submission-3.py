class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in value_index:
                return [value_index[difference], i]
            else:
                value_index[nums[i]] = i

            