# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum = ListNode(None, head)
        prev, curr = dum, head

        while curr:
            save = curr.next
            if curr.val == val:
                prev.next = save
            else:
                prev = curr
            
            curr = save

        return dum.next