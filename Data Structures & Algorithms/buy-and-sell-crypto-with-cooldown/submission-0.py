class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        
        buy = [0] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        cooldown = [0] * (len(prices) + 1)
        buy[0] = -prices[0]

        for i in range(1, len(prices) + 1):

            buy[i] = max(cooldown[i - 1] - prices[i - 1], buy[i - 1]) 
            sell[i] = prices[i - 1] + buy[i - 1]
            cooldown[i] = max(sell[i - 1], cooldown[i - 1])

    
        return max(sell[len(prices)], cooldown[len(prices)])
