class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # If total sum is odd, impossible to partition into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[j] = True if we can form sum j using a subset of the numbers seen so far
        dp = [False] * (target + 1)
        dp[0] = True  # sum 0 is always possible (empty subset)
        
        for num in nums:
            # Traverse backwards to avoid using the same number multiple times
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            
            # Early exit if target is already reachable
            if dp[target]:
                return True
        
        return dp[target]