from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Right half is unsorted → minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Left half (including mid) is sorted → minimum is in the left half (or mid)
            else:
                right = mid
        
        return nums[left]