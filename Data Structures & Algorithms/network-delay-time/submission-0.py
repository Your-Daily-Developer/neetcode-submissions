from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list: node → list of (neighbor, weight)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist[i] = shortest time from k to i
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        # Min-heap of (time, node)
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            # Skip if we already found a better path
            if time > dist[node]:
                continue

            for nei, w in graph[node]:
                new_time = time + w
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1