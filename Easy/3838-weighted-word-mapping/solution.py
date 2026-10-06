class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res=""
        for i in words:
            sums=0
            for j in i:
                sums+=weights[ord(j)-97]
            res+=chr(25-(sums%26)+97)
        return res
