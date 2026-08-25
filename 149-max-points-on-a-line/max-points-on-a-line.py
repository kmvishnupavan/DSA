class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        ans = 1

        for i in range(n):
            slopes = {}

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1

                slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

                ans = max(ans, slopes[slope] + 1)

        return ans