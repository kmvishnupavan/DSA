class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.s = s
        self.build(1, 0, self.n - 1)

    def build(self, node, left, right):
        if left == right:
            ch = self.s[left]
            self.tree[node] = (ch, ch, 1, 1, 1, 1)
            return

        mid = (left + right) // 2

        self.build(node * 2, left, mid)
        self.build(node * 2 + 1, mid + 1, right)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def merge(self, a, b):
        # a = (leftChar, rightChar, leftLen, rightLen, best, length)
        # b = (leftChar, rightChar, leftLen, rightLen, best, length)

        a_left_char, a_right_char, a_left_len, a_right_len, a_best, a_len = a
        b_left_char, b_right_char, b_left_len, b_right_len, b_best, b_len = b

        left_char = a_left_char
        right_char = b_right_char

        left_len = a_left_len
        right_len = b_right_len

        best = max(a_best, b_best)

        if a_right_char == b_left_char:
            best = max(best, a_right_len + b_left_len)

            # Entire left segment has the same character
            if a_left_len == a_len:
                left_len = a_len + b_left_len

            # Entire right segment has the same character
            if b_right_len == b_len:
                right_len = b_len + a_right_len

        return (
            left_char,
            right_char,
            left_len,
            right_len,
            best,
            a_len + b_len
        )

    def update(self, node, left, right, index, ch):
        if left == right:
            self.tree[node] = (ch, ch, 1, 1, 1, 1)
            return

        mid = (left + right) // 2

        if index <= mid:
            self.update(node * 2, left, mid, index, ch)
        else:
            self.update(node * 2 + 1, mid + 1, right, index, ch)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def change(self, index, ch):
        self.update(1, 0, self.n - 1, index, ch)

    def get_best(self):
        return self.tree[1][4]


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        seg = SegmentTree(s)

        ans = []

        for ch, index in zip(queryCharacters, queryIndices):
            seg.change(index, ch)
            ans.append(seg.get_best())

        return ans