class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            # Calculate the three candidates
            candidates = [
                curr,                     # start a new subarray
                max_so_far * curr,        # continue with previous max
                min_so_far * curr         # continue with previous min (important for negatives!)
            ]

            # Update max and min for next iteration
            max_so_far = max(candidates)
            min_so_far = min(candidates)

            # Keep the global answer
            result = max(result, max_so_far)

        return result