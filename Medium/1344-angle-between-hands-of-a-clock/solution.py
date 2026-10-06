class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        a=abs((hour*30)-(5.5*minutes))
        b=360-a
        return min(a,b)
