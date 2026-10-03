from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()          # stores indices
        res = []

        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window
            if q and q[0] == i - k:
                q.popleft()

            # 2. Maintain decreasing order: remove smaller elements from the back
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            # 3. Once the window is fully formed, record the max
            if i >= k - 1:
                res.append(nums[q[0]])

        return res