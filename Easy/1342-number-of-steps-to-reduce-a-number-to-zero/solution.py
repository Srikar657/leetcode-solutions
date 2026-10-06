class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        while num:
            if num%2==0:
                c+=1
                num//=2
            else:
                c+=1
                num-=1
        return c
