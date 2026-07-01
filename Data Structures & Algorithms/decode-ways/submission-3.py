class Solution:
    def numDecodings(self, s: str) -> int:
        
        def findPaths(index, memo):
            if index in memo:
                return memo[index]

            

            if index >= len(s):
                return 1
            
            if index == len(s) - 1:
                if s[index] == '0':
                    return 0
                else:
                    return 1

            if s[index] == '0':
                return 0

            

            single_digit_branch_paths = findPaths(index + 1, memo)

            two_digit_number = int(s[index] + s[index + 1])
            double_digit_branch_paths = 0
            if two_digit_number < 27 and two_digit_number > 9:
                double_digit_branch_paths = findPaths(index + 2, memo)

            memo[index] = single_digit_branch_paths + double_digit_branch_paths

            return memo[index]


        memo = {}
        return findPaths(0, memo)
        

        