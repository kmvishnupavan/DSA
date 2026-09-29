class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # If starting cell is ')', balance becomes negative
        if grid[0][0] == ')':
            return False

        # dp[j] = set of possible balances at current row, column j
        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                new_set = set()

                # From top
                if i > 0:
                    for balance in dp[j]:
                        new_balance = balance + (1 if grid[i][j] == '(' else -1)
                        if new_balance >= 0:
                            new_set.add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[j - 1]:
                        new_balance = balance + (1 if grid[i][j] == '(' else -1)
                        if new_balance >= 0:
                            new_set.add(new_balance)

                dp[j] = new_set

        return 0 in dp[n - 1]
        