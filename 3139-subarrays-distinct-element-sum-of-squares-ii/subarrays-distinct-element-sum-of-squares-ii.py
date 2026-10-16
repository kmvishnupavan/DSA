
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                length = end - start + 1
                old_sum = tree_sum[node]

                tree_sq[node] = (
                    tree_sq[node] + 2 * old_sum + length
                ) % MOD

                tree_sum[node] = (old_sum + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2
            lc = node * 2
            rc = lc + 1

            if lazy[node]:
                val = lazy[node]

                for child, l, r in (
                    (lc, start, mid),
                    (rc, mid + 1, end)
                ):
                    length = r - l + 1
                    old_sum = tree_sum[child]

                    tree_sq[child] = (
                        tree_sq[child]
                        + 2 * val * old_sum
                        + val * val * length
                    ) % MOD

                    tree_sum[child] = (
                        old_sum + val * length
                    ) % MOD

                    lazy[child] += val

                lazy[node] = 0

            update(lc, start, mid, left, right)
            update(rc, mid + 1, end, left, right)

            tree_sum[node] = (
                tree_sum[lc] + tree_sum[rc]
            ) % MOD

            tree_sq[node] = (
                tree_sq[lc] + tree_sq[rc]
            ) % MOD

        last = {}
        ans = 0

        for r, num in enumerate(nums):
            prev = last.get(num, -1)

            update(1, 0, n - 1, prev + 1, r)

            ans = (ans + tree_sq[1]) % MOD
            last[num] = r

        return ans
