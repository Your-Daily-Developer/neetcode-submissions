class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        s = sum(nums)
        if s < abs(target) or (s + target) % 2:
            return 0
        P = (s + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]   