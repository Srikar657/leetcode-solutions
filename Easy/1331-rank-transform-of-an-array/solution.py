class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_rank = sorted(set(arr))
        rank_map={num : i+1 for i , num in enumerate(sorted_rank)}
        return [rank_map[num] for num in arr]
        
