class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prof = 1e9+7
        max_prof = 0

        for i in range(len(prices)):
            min_prof = min(min_prof,prices[i])
            profit = prices[i]-min_prof
            max_prof  = max(profit,max_prof)

        
        return max_prof