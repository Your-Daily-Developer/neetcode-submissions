class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Our "memory" bank
        
        for i, num in enumerate(nums):
            needed = target - num  # Calculate the complement
            
            if needed in seen:
                # We found the number we needed earlier!
                return [seen[needed], i]
            
            # Store the current number for future checks
            seen[num] = i
            
        return []   