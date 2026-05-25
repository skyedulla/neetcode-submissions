class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > highest_profit:
                    highest_profit = profit
        return highest_profit
                

        