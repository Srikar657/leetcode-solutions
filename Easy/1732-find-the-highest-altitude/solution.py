class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        result=[0]
        temp=0
        for i in gain:
            temp=i+temp
            result.append(temp)
        return max(result)
