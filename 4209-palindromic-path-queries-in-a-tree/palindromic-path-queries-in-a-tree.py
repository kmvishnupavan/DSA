class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p

                for j in range(1, LOG):
                    parent[j][u] = parent[j - 1][parent[j - 1][u]]

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        def lca(u, v):
            if ancestor(u, v):
                return u
            if ancestor(v, u):
                return v

            for j in range(LOG - 1, -1, -1):
                x = parent[j][u]
                if not ancestor(x, v):
                    u = x

            return parent[0][u]

        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_xor(left, right):
            result = prefix(right)
            if left > 0:
                result ^= prefix(left - 1)
            return result

        chars = list(s)
        masks = [1 << (ord(c) - ord('a')) for c in chars]

        for u in range(n):
            add(tin[u], masks[u])

        for u in range(n):
            if tout[u] + 1 < n:
                add(tout[u] + 1, masks[u])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))
                delta = masks[u] ^ new_mask

                if delta:
                    add(tin[u], delta)
                    if tout[u] + 1 < n:
                        add(tout[u] + 1, delta)

                    chars[u] = c
                    masks[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask_u = range_xor(tin[w], tin[u])
                mask_v = range_xor(tin[w], tin[v])

                mask = mask_u ^ mask_v ^ masks[w]

                answer.append((mask & (mask - 1)) == 0)

        return answer