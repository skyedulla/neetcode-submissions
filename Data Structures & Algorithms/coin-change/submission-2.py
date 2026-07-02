class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin > 0:
                    if dp[i - coin] != float('inf'):
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]