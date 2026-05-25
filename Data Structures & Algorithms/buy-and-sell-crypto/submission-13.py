class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        highest_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > highest_profit:
                highest_profit = profit
            if profit < 0:
                left = right
            right += 1
        return highest_profit