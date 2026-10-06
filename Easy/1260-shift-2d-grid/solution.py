class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m , n = len(grid) , len(grid[0])
        total=m*n
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k%=total
        flat = flat[-k:]+flat[:-k]
        res=[]
        for i in range(m):
            row=flat[i*n:(i+1)*n]
            res.append(row)
        return res
        
