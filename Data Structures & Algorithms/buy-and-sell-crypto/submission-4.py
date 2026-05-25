class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        left = 0
        while left < len(prices) - 1:
            right = left + 1
            while right < len(prices):
                profit = prices[right] - prices[left]
                if profit > highest_profit:
                    highest_profit = profit
                right += 1
            left += 1
        return highest_profit
                

        