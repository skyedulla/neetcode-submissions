class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        profit = 0
        while right < len(prices):
            profit = max(profit,prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit