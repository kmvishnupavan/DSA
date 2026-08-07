from dataclasses import dataclass
import itertools


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
        self.st[0] = nums.copy()

        for i in range(1, self.n.bit_length() + 1):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j],
                    self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l, r):
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries):
        ones = s.count('1')

        zeroGroups, zeroGroupIndex = self._getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        st = SparseTable(self._getZeroMergeLengths(zeroGroups))

        def solve(l, r):
            left = (
                -1
                if zeroGroupIndex[l] == -1
                else zeroGroups[zeroGroupIndex[l]].length
                - (l - zeroGroups[zeroGroupIndex[l]].start)
            )

            right = (
                -1
                if zeroGroupIndex[r] == -1
                else r - zeroGroups[zeroGroupIndex[r]].start + 1
            )

            start = zeroGroupIndex[l] + 1
            end = (
                zeroGroupIndex[r]
                if s[r] == '1'
                else zeroGroupIndex[r] - 1
            )

            ans = ones

            if (
                s[l] == '0'
                and s[r] == '0'
                and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                ans = max(ans, ones + left + right)

            elif start <= end - 1:
                ans = max(ans, ones + st.query(start, end - 1))

            if (
                s[l] == '0'
                and zeroGroupIndex[l] + 1
                <= (
                    zeroGroupIndex[r]
                    if s[r] == '1'
                    else zeroGroupIndex[r] - 1
                )
            ):
                ans = max(
                    ans,
                    ones
                    + left
                    + zeroGroups[zeroGroupIndex[l] + 1].length,
                )

            if (
                s[r] == '0'
                and zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                ans = max(
                    ans,
                    ones
                    + right
                    + zeroGroups[zeroGroupIndex[r] - 1].length,
                )

            return ans

        return [solve(l, r) for l, r in queries]

    def _getZeroGroups(self, s):
        groups = []
        idx = []

        for i, c in enumerate(s):
            if c == '0':
                if i > 0 and s[i - 1] == '0':
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        return groups, idx

    def _getZeroMergeLengths(self, groups):
        return [a.length + b.length for a, b in itertools.pairwise(groups)]