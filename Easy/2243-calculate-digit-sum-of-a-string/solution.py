class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def div(s,k):
            res=""
            j=0
            q=0
            for i in s:
                if q!=k:
                    j+=int(i)
                    q+=1
                else:
                    res+=str(j)
                    q=1
                    j=int(i)
            res+=str(j)
            return res
        while len(s)>k:
            s=div(s,k)
        return s
        
