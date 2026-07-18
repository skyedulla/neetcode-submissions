class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        visited = [False] * len(nums)
        def copyPermutations(curr_perm):

            if len(curr_perm) == len(nums):
                perms.append(curr_perm.copy())
                return



            for i in range(len(nums)):
                if visited[i] == False:
                    curr_perm.append(nums[i])
                    visited[i] = True
                    copyPermutations(curr_perm)
                    visited[i] = False
                    curr_perm.pop()

        copyPermutations([])
        return perms
 


    """ Permutations require accessing prior numbers in the array
    after the initial array already processed it in the first position.
    each value will go then. However the call stack needs to pass 
    down which elements are already in the array """