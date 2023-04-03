# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dum = ListNode(None,head)

        prev,curr = head, head.next

        while curr:
            save = curr.next

            if prev.val == curr.val:
                prev.next = save
            else:
                prev = curr
            
            curr = save
        
        return dum.next