class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        arr=sorted(arr)
        min_diff=float('inf')
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            if diff<min_diff:
                min_diff=diff
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min_diff:
                res.append([arr[i],arr[i+1]])
        return res
                    
