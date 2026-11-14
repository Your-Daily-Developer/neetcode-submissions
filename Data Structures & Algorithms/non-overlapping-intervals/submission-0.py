class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by ending time
        intervals.sort(key=lambda x: x[1])
        
        count = 0          # number of intervals we keep
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:          # no overlap
                count += 1
                prev_end = end
        
        # Minimum removals = total - maximum we can keep
        return len(intervals) - count