class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result