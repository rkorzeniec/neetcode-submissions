class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) < 1:
            return profit
            
        buy = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                day_profit = prices[i] - prices[buy]
                profit = max(profit, day_profit)

        return profit
