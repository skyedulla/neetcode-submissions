class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        nums.sort()

        def dfs(current_path, index):
            subsets.append(current_path.copy())
            
            if index == len(nums):
                return
            



            for i in range(index, len(nums)):
                #The reason why i needs to be greater than index is to ensure that
                #new decision levels process combinations with the duplicates, but not
                #further duplicates in the same level because that will lead to duplicates
                #since the loop will process the first 2 and the second 2 at the same level 
                #for example.
                if i > index and nums[i] == nums[i - 1]:
                    continue
                current_path.append(nums[i])
                dfs(current_path, i + 1)
                current_path.pop()
        
        dfs([], 0)
        return subsets