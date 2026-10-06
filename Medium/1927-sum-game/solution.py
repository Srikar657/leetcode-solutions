class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        half=n//2
        suml,sumr=0,0
        ql,qr=0,0
        for i in range(half):
            if num[i] == '?':
                ql+=1
            else:
                suml+=int(num[i])
        for i in range(half,n):
            if num[i]=='?':
                qr+=1
            else:
                sumr+=int(num[i])
        diffsum=suml-sumr
        diffq=qr-ql
        if diffq%2==0 and diffsum == (diffq//2)*9:
            return False
        return True
