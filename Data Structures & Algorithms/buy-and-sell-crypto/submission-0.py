from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: if there are no prices or only one day, no profit can be made
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:  # 'price' is the actual value (e.g., 7, 1, 5...)
            # If we find a lower buying price, update our minimum baseline
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
