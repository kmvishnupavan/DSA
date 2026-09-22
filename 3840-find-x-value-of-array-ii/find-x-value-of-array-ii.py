class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        tree = [[1 % k, [0] * k] for _ in range(2 * size)]

        def make_node(val):
            r = val % k
            cnt = [0] * k
            cnt[r] = 1
            return [r, cnt]

        def merge(a, b):
            prod_a, cnt_a = a
            prod_b, cnt_b = b

            prod = (prod_a * prod_b) % k
            cnt = cnt_a[:]

            for r in range(k):
                new_r = (r * prod_a) % k
                cnt[new_r] += cnt_b[r]

            return [prod, cnt]

        # Build the segment tree
        for i in range(n):
            tree[size + i] = make_node(nums[i])

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(index, val):
            pos = size + index
            tree[pos] = make_node(val)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(left, right):
            # Query the half-open interval [left, right)
            left += size
            right += size

            res_left = [1 % k, [0] * k]
            res_right = [1 % k, [0] * k]

            while left < right:
                if left % 2:
                    res_left = merge(res_left, tree[left])
                    left += 1

                if right % 2:
                    right -= 1
                    res_right = merge(tree[right], res_right)

                left //= 2
                right //= 2

            return merge(res_left, res_right)

        result = []

        for index, value, start, x in queries:
            # Apply the persistent point update
            nums[index] = value
            update(index, value)

            # Count non-empty prefixes of nums[start:]
            if start == n:
                result.append(0)
            else:
                res = query(start, n)
                result.append(res[1][x])

        return result