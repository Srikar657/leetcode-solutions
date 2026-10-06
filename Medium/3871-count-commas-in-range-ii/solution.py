class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        c = 0
        if len(s) - 1 < 3:
            return 0
        if n > 999:
            q = n - 999
            k = q
            if n - 999999 >= 0:
                q = 999999 - 999
                k = q
            c += k * 1
        if n > 999999:
            q = n - 999999
            k = q
            if n - 999999999 >= 0:
                q = 999999999 - 999999
                k = q
            c += k * 2
        if n > 999999999:
            q = n - 999999999
            k = q
            if n - 999999999999 >= 0:
                q = 999999999999 - 999999999
                k = q
            c += k * 3
        if n > 999999999999:
            q = n - 999999999999
            k = q
            if n - 999999999999999 >= 0:
                q = 999999999999999 - 999999999999
                k = q
            c += k * 4
        if n > 999999999999999:
            q = n - 999999999999999
            k = q
            c += k * 5
        return c
        
