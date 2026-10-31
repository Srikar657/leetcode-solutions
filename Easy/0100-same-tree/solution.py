# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        result=[]
        def preorder(node1,node2):
            if not node1 and not node2:  
                return
            if not node1 or not node2:
                result.append(False)
                return
            result.append(node1.val==node2.val)
            preorder(node1.left,node2.left)
            preorder(node1.right,node2.right) 
        preorder(p,q)
        if False in result:
            return False
        else:
            return True
