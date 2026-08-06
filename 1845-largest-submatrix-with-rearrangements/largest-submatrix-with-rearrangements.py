class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Build histogram heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0

        for row in matrix:
            heights = sorted(row, reverse=True)

            for j, h in enumerate(heights):
                ans = max(ans, h * (j + 1))

        return ans