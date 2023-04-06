# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bfs:
        
        if not root : return 0
        q = deque([(root, 1)])

        while q:
            node,num = q.popleft()
            if not node.left and not node.right: return num
            if node.left: q.append((node.left, num+1))
            if node.right: q.append((node.right, num+1))

        
        
        
        ## dfs:
        if not root: return 0

        self.small = float('inf')

        def dfs(node, h):
            if not node: return 
            if not node.left and not node.right:
                self.small = min(self.small, h)
            dfs(node.left, h+1)
            dfs(node.right, h+1)

        dfs(root, 1)

        return self.small











