# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i

        self.postIndex = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            rootVal = postorder[self.postIndex]
            self.postIndex -= 1

            root = TreeNode(rootVal)

            mid = inorderMap[rootVal]

            # Build right subtree first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1) 