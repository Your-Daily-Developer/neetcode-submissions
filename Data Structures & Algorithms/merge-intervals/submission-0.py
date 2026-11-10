from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]

            # If current overlaps with the last merged interval
            if current[0] <= last[1]:
                # Merge them by updating the end
                last[1] = max(last[1], current[1])
            else:
                # No overlap → add as a new interval
                merged.append(current)

        return merged