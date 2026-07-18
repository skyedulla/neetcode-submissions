class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []

        def combinationsVariableSize(curr_comb, index):
            subsets.append(list(curr_comb))

            if index  >= len(nums):
                return
            
            


            for i in range(index, len(nums)):
                curr_comb.append(nums[i])
                combinationsVariableSize(curr_comb, i + 1)
                curr_comb.pop()

        combinationsVariableSize([], 0)
        return subsets