class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        res= []
        j = 0
        for i in pushed:
            res.append(i)
            while res and res[-1] == popped[j]:
                res.pop()
                j += 1
        return len(res) == 0
