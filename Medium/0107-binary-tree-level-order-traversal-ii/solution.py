# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self,root):
        r=[]
        k=[]
        if root is None:
            return []
        queue=[]
        queue.append(root)
        queue.append(None)
        while queue:
            curr=queue.pop(0)
            if curr is None:
                if len(queue)==0:
                    break;
                else:
                    queue.append(None)
                    r.append(k)
                    k=[]
            else:
                k.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        r.append(k)  
        return r[::-1]
