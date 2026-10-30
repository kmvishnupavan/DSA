
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # State: (cost, node, last_char, consecutive_count)
        pq = [(0, 0, labels[0], 1)]

        dist = {}

        while pq:
            cost, node, last, count = heapq.heappop(pq)

            state = (node, last, count)

            if state in dist and dist[state] <= cost:
                continue

            dist[state] = cost

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                ch = labels[nxt]

                if ch == last:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_state = (nxt, ch, new_count)

                if new_state not in dist or cost + weight < dist[new_state]:
                    heapq.heappush(
                        pq,
                        (cost + weight, nxt, ch, new_count)
                    )

        return -1
