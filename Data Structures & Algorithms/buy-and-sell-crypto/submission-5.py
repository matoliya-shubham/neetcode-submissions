class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice, maxprofit = float('inf'), 0
        for curr_price in prices:
            minprice = min(minprice, curr_price)
            curr_profit = curr_price - minprice
            maxprofit = max(maxprofit, curr_profit)
        return maxprofit


