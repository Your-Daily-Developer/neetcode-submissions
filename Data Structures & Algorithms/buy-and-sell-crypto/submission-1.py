class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_possible = float('inf')
        max_profit = 0

        for i in prices:
            if i < max_possible:
                max_possible = i
            if i - max_possible > max_profit:
                max_profit = i - max_possible

        return max_profit
        