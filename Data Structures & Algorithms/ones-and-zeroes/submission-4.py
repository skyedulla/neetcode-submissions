class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def choose(i, m, n):
            state = (i, m, n)
            if state in memo:
                return memo[state]

            if i == len(strs):
                return 0

            zero_count = 0
            one_count = 0
            for char in strs[i]:
                if char == "0":
                    zero_count += 1
                else:
                    one_count += 1
            
            skip = choose(i + 1, m, n)

            take = 0
            if m - zero_count >= 0 and n - one_count >= 0:
                take = 1 + choose(i + 1, m - zero_count, n - one_count)

            memo[state] = max(take, skip)

            return memo[state]
        
        return choose(0, m, n)
        