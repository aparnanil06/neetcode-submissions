class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices): 
            if prices[l] < prices[r]:
                output = prices[r] - prices[l]
                profit = max(profit, output)
            else:
                l = r #l moves to r if r if greater than l
            r += 1 #r always moves right 1
        return profit    

