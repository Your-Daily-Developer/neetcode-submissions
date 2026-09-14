class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
                max_streak = max(max_streak, current)
            else:
                current = 0

        return max_streak