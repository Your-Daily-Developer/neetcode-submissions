class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0      # end of the current jump range
        farthest = 0         # farthest we can reach so far
        
        # We don't need to process the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit (optional optimization)
                if current_end >= len(nums) - 1:
                    break
        
        return jumps                        