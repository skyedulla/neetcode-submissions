class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        array = []

        def dfs(zeros_left, ones_left, current_path):
            if ones_left < zeros_left:
                return
            if zeros_left == 0 and ones_left == 0:
                array.append(current_path.copy())
                return


            if zeros_left > 0:
                current_path.append('(')
                dfs(zeros_left - 1, ones_left, current_path)
                current_path.pop()


            if ones_left > 0:
                current_path.append(')')
                dfs(zeros_left, ones_left - 1, current_path)
                current_path.pop()

            

        dfs(n, n, [])
        parentheses = ["".join(p) for p in array]
        return parentheses

            


