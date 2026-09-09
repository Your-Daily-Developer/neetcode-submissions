from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # sort by frequency descending and take the first k keys
        return [num for num, _ in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]