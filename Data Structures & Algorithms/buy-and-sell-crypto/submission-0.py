class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        for i in range(len(prices)- 1):
            print(prices[i+1:len(prices)])
            MaxProfit = max(MaxProfit,max(prices[i+1:len(prices)]) - prices[i])
        return MaxProfit
        
        