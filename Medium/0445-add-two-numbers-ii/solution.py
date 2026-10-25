# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s1=[]
        s2=[]
        temp1=l1
        temp2=l2
        while temp1 is not None:
            s1.append(temp1.val)
            temp1=temp1.next
        while temp2 is not None:
            s2.append(temp2.val)
            temp2=temp2.next
        c = 0
        head = None
        while s1 or s2 or c:
            t = c
            if s1:
                t += s1.pop()
            if s2:
                t += s2.pop()
            c = t // 10
            n = ListNode(t % 10)
            n.next = head
            head = n
        return head
