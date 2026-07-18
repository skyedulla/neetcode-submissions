class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}

        letter_combs = []

        def dialCombos(d_index, path):
            if len(path) == len(digits):
                letter_combs.append(path.copy())
                return


            for letter in letter_map[digits[d_index]]:
                path.append(letter)
                dialCombos(d_index + 1, path)
                path.pop()


        dialCombos(0, [])
        letter_combs = ["".join(array) for array in letter_combs]
        return letter_combs

        


