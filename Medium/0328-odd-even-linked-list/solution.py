# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        s=head
        f=head.next
        q=f
        while f and f.next:
            s.next = f.next
            s=s.next
            f.next=s.next
            f=f.next
        s.next=q
        return head
        
