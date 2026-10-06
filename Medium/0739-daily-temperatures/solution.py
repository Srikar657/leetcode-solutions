class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        x=len(temperatures)
        ans =[0]*x
        stack=[]
        for i in range(x):
            found=0
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i-prev
            stack.append(i)
        return ans
