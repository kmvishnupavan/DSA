class Solution:
    def findKthSmallest(self, coins, k):
        from math import gcd

        n = len(coins)

        # Remove redundant coins.
        # If a coin is a multiple of another coin,
        # it does not create any new amounts.
        coins.sort()
        useful = []

        for c in coins:
            redundant = False
            for x in useful:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        # Count how many positive integers <= x
        # are divisible by at least one coin.
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                value = x // lcm

                if bits % 2 == 1:
                    total += value
                else:
                    total -= value

            return total

        # Binary search answer.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left