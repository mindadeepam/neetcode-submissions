class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price_yet = prices[0]
        max_profits = 0

        for i, curr_price in enumerate(prices):
            if i==0:
                continue

            if least_price_yet<curr_price:
                profits = curr_price - least_price_yet
                max_profits = max(max_profits, profits)

            least_price_yet = min(curr_price, least_price_yet)
        
        return max_profits