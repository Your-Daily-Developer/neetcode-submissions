class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])  # append a copy
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]  # choose
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]  # undo

        backtrack(0)
        return res   