class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Pacific (top row)
        for c in range(cols):
            dfs(0, c, pacific)

        # Pacific (left column)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic (bottom row)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Atlantic (right column)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans