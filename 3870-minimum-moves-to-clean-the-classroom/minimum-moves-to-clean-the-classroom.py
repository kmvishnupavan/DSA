from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)

        if total == 0:
            return 0

        target = (1 << total) - 1

        # state = (row, col, remaining_energy, collected_mask)
        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        # Store the maximum energy reached for each position and mask.
        visited = {}
        visited[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c, e, mask = queue.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    ne = e - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        new_mask |= 1 << litter[(nr, nc)]

                    # Reset energy at R
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, new_mask)

                    # If we have already reached this state with
                    # equal or more energy, this state is unnecessary.
                    if state in visited and visited[state] >= ne:
                        continue

                    visited[state] = ne
                    queue.append((nr, nc, ne, new_mask))

            moves += 1

        return -1