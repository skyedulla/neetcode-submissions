class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
            



        """if low is not less than high then it must be equal to high and they both 
        must contain the target for the target to be in nums"""
        if low == high and nums[low] == target:
            return low
        else:
            return -1

        