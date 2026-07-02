class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """chooseStair will find the cost of the choosing to step from curr_stair + 1 or curr_stair + 2
        if the stair is the last stair then the cost isn't counted. 

        If the stair is len(stairs) - 2 then there is only one choice 

        chooseStair adds the value of the step that is currently being stepped on because the cost
        is based on the stair that is being stepped on not the stair that is being stepped to"""
        memo = {}
        def chooseStair(index):
            if index in memo:
                return memo[index]

            if index >= len(cost): 
                return 0
            

            one_step = cost[index] + chooseStair(index + 1)
            two_steps = cost[index] + chooseStair(index + 2)

            memo[index] = min(one_step, two_steps)

            return memo[index]
        
        return min(chooseStair(0), chooseStair(1))

        