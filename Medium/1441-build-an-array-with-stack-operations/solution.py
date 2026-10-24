class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack=[]
        for i in range(1,n+1):
            if i in target:
                stack.append("Push")
            elif i not in target and i<=target[-1]:
                stack.append("Push")
                stack.append("Pop")
        return stack
