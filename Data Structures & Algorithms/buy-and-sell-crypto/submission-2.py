class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        p1 = 0
        p2 = 1
        profit_max = 0 

        while p2 < len(prices):
            if prices[p1] < prices[p2]:
                profit = prices[p2] - prices[p1]
                if profit > profit_max:
                    profit_max = profit
            else:
                p1 = p2
            
            p2 += 1

        return profit_max


