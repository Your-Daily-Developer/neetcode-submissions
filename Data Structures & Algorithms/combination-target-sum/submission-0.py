from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], remaining: int):
            # Base cases
            if remaining == 0:
                result.append(path[:])   # found a valid combination
                return
            if remaining < 0:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # We can reuse the same number, so pass 'i' (not i+1)
                backtrack(i, path, remaining - candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], target)
        return result