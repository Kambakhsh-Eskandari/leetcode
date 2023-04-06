# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        self.t = targetSum
        
        s = [(root, root.val)]
        while s:
            node,v = s.pop()
            if not node.left and not node.right and v==self.t:
                return True
            if node.left:
                s.append((node.left, v+node.left.val))
            if node.right:
                s.append((node.right, v+node.right.val))
        return False

        # self.t = targetSum
        # def dfs(node, s):
        #     if not node: return False

        #     s += node.val
        #     if not node.left and not node.right:
        #         return self.t == s

        #     return (dfs(node.right, s) or dfs(node.left, s))
        
        # return dfs(root,0)
        

