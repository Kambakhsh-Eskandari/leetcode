## T(n), O(n) solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mem = []
        while head:
            mem.append(head.val)
            head = head.next
        l,r = 0, len(mem) - 1
        while l < r:
            if mem[l] != mem[r]:
                return False
            l+=1
            r-=1
        return True
    

## T(n), O(1) solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# find the middle of linkedlist
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half:
        prev, curr = None, slow

        while curr:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save
        
        while head and prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        
        return True