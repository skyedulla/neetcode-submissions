class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates.sort()
        valid_combs = []

        
        def backtrack(curr_comb, starting_index, total):
            if sum(curr_comb) > target:
                return
            elif sum(curr_comb) == target:
                valid_combs.append(list(curr_comb))
                return
            
            if starting_index >= len(candidates):
                return


            
            for i in range(starting_index, len(candidates)):
                if i > starting_index and candidates[i] == candidates[i - 1]:
                    continue

                curr_comb.append(candidates[i])
                total += candidates[i]
                backtrack(curr_comb, i + 1, total)
                total -= candidates[i]
                curr_comb.pop()

        backtrack([], 0, 0)
            
        return valid_combs


    """ Our algorithm currently skips duplicates, which results in missing combinations
    involving two of the same numbers. Therefore we need to remove the code that skips
    the duplicates. However now will our algorithm return two versions of the combinations?
    I don't believe so because with our current code the call stack completly prevents 
    reusing the same number """