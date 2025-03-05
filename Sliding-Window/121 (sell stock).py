class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        """max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if ((prices[j] - prices[i]) > max_profit) and (j>i):
                    max_profit = prices[j] - prices[i]
        
        return max_profit"""

        # low memory
        """left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
                
            right += 1

        return max_profit"""

        # low time complex
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
    