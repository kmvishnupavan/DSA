class Solution:
    def getHappyString(self, n, k):
        ans = []

        def dfs(path):
            if len(path) == n:
                ans.append("".join(path))
                return

            for ch in "abc":
                if not path or path[-1] != ch:
                    path.append(ch)
                    dfs(path)
                    path.pop()

        dfs([])

        if k > len(ans):
            return ""

        return ans[k - 1]