# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        c=0
        temp=head
        while temp is not None:
            c+=1
            temp=temp.next
        i=1
        temp=head
        prev=None
        while i<(c-n+1) and temp is not None:
            prev=temp
            temp=temp.next
            i+=1
        if prev == None:
            return head.next
        prev.next=temp.next
        return head
