class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=[]
        for i in (nums):
            if(i%2==0):
                s.append(i)
        d={}
        for i in s:
            d[i]=s.count(i)
        if not d:
            return -1
        max1=max(d.values())
        c= [num for num,freq in d.items() if freq == max1]
        return min(c)
