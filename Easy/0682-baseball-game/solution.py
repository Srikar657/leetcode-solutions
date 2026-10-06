class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res=[]
        for op in operations:
            if op == 'C':
                res.pop()
            elif op=='D':
                res.append(2*res[-1])
            elif op == '+':
                res.append(res[-1]+res[-2])
            else:
                res.append(int(op))
        return sum(res)
