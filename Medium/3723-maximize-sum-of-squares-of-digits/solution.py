class Solution(object):
    def maxSumOfSquares(self, num, sums):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sums > 9 * num:
            return ""
        res = []
        for _ in range(num):
            digit = min(9, sums)
            res.append(str(digit))
            sums -= digit
        return "".join(res)
