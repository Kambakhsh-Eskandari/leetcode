# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        S = defaultdict(float)
        H = defaultdict(int)
        def dfs(node, h):
            if not node: return 
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            S[h] += node.val
            H[h] += 1

        dfs(root,0)
        return [S[i]/H[i] for i in range(len(S))]

        