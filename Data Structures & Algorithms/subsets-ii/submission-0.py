class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                     # Sort to group duplicates
        result = []
        
        def backtrack(start: int, path: list[int]):
            result.append(path[:])      # Add a copy of the current subset
            
            for i in range(start, len(nums)):
                # Skip duplicates: if current number is same as previous
                # and we are at the same level, skip it
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()              # backtrack
        
        backtrack(0, [])
        return result