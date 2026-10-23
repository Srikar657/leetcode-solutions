# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s=head
        f=head
        prev=None
        while f and f.next:
            s=s.next
            f=f.next.next
        curr=s.next
        s.next=None
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        temp=head
        while prev:
            nxt = head.next
            p = prev.next
            head.next = prev
            prev.next = nxt
            head = nxt
            prev = p
        return head
