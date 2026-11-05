class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+2)
        def fib(n,dp):
            if n==0 or n==1:
                dp[n]=n
                return dp[n]
            if dp[n] != -1:
                return dp[n]
            dp[n]=fib(n-1,dp)+fib(n-2,dp)
            return dp[n]
        return fib(n+1,dp)
