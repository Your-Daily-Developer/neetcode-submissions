from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt = Counter(tasks)
        x = max(cnt.values())                        # max frequency
        s = sum(v == x for v in cnt.values())        # # of tasks with max freq
        return max(len(tasks), (x - 1) * (n + 1) + s)   