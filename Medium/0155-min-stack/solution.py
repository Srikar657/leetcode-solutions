class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.mins=[]
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.stack.append(value)
            self.mins.append(value)
        else:
            self.stack.append(value)
            self.mins.append(min(self.mins[-1],value))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
