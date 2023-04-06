# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # ans 1:
        if not q and not p: return True
        if not q or not p: return False

        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

        # ans 2:
        s = [(p,q)]
        while s:
            n1, n2 = s.pop()
            if not n1 and not n2: pass
            elif not n1 or not n2: return False
            else:
                if n1.val != n2.val : return False
                s.append((n1.left,n2.left))
                s.append((n1.right,n2.right))
        
        return True
