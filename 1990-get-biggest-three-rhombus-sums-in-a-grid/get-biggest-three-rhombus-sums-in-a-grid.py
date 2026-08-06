class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])

        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]

        for i in range(m):
            for j in range(n - 1, -1, -1):
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        ans = set()

        for i in range(m):
            for j in range(n):
                ans.add(grid[i][j])

                k = 1
                while (
                    i - k >= 0 and
                    i + k < m and
                    j - k >= 0 and
                    j + k < n
                ):
                    s1 = diag1[i + 1][j + k + 1] - diag1[i - k][j]
                    s2 = diag2[i + k + 1][j] - diag2[i][j + k + 1]
                    s3 = diag1[i + k + 1][j + 1] - diag1[i][j - k]
                    s4 = diag2[i + 1][j - k] - diag2[i - k][j + 1]

                    total = (
                        s1 + s2 + s3 + s4
                        - grid[i - k][j]
                        - grid[i][j + k]
                        - grid[i + k][j]
                        - grid[i][j - k]
                    )

                    ans.add(total)
                    k += 1

        return sorted(ans, reverse=True)[:3]