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
        def to_list(w):
            r=[]
            while w:
                r.append(w.val)
                w=w.next
            return r
        res=[]
        r1=""
        r2=to_list(l1)
        r3=""
        r4=to_list(l2)
        for i in r2:
            r1+=str(i)
        for i in r4:
            r3+=str(i)
        r1=r1[::-1]
        r3=r3[::-1]
        m=str(int(r1)+int(r3))[::-1]
        d = ListNode()
        c = d
        for i in m:
            c.next = ListNode(int(i))
            c = c.next
        return d.next
