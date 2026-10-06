class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        cost = 0
        for i in range(0,n,8):
            layer_size = min(8 , n-i)
            cost += (i/8+1)*layer_size
        return cost
