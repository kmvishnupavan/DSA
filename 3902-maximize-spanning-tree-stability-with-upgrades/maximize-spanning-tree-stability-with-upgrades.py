class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

        self.components -= 1
        return True


class Solution:
    def maxStability(self, n, edges, k):
        maxStrength = max(s for _, _, s, _ in edges)

        def check(x):
            dsu = DSU(n)

            # mandatory edges
            for u, v, s, must in edges:
                if must:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False

            # free optional edges
            for u, v, s, must in edges:
                if not must and s >= x:
                    dsu.union(u, v)

            upgrades = 0

            # upgraded edges
            for u, v, s, must in edges:
                if must:
                    continue

                if s < x and 2 * s >= x:
                    if dsu.union(u, v):
                        upgrades += 1
                        if upgrades > k:
                            return False

            return dsu.components == 1

        lo = 1
        hi = 2 * maxStrength
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans