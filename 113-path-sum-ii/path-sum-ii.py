class Solution:
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, curr_sum, path):
            if not node:
                return

            path.append(node.val)
            curr_sum += node.val

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    ans.append(path[:])
            else:
                dfs(node.left, curr_sum, path)
                dfs(node.right, curr_sum, path)

            path.pop()

        dfs(root, 0, [])
        return ans