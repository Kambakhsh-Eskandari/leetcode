# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.h = 0

        def dfs(node):
            if not node: return -1

            l = dfs(node.left)
            r = dfs(node.right)

            self.h = max(self.h, 2+l+r)

            return 1 + max(l,r)

        dfs(root)
        return self.h