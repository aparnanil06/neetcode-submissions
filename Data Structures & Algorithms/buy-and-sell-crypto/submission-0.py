class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        i = len(prices) - 1
        while i > 0:
            output = prices[i] - min(prices[:i])
            if output > profit:
                profit = output
            i -= 1
        if profit <= 0:
            return 0
        return profit
