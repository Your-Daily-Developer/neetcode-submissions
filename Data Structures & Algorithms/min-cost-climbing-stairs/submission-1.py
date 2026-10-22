class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        # dp[i] = min cost to reach step i
        # You can reach step i from step i-1 or step i-2
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]   