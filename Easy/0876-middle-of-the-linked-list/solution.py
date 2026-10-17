# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=None
        s=head
        f=head
        if head.next is None:
            return head
        while f and f.next:
            s=s.next
            temp=s
            f=f.next.next
        return temp
