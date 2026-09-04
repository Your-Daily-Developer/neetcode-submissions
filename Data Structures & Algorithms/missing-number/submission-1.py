class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        value = sum(nums)
        total = 0
        n = len(nums)
        for i in range(n + 1):
            total += i

        return total - value
