class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        for j in range(l):
            i=l-1
            a=[]
            while i>=0:
                a+=[matrix[i][j]]
                i-=1
            matrix+=[a]
        for i in range(l):
            matrix.pop(0)
        
