class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = {}
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - ord('a'))
            masks[mask] = max(masks.get(mask, 0), len(w))
        max_prod = 0
        mask_list = list(masks.items())
        for i in range(len(mask_list)):
            for j in range(i+1, len(mask_list)):
                if mask_list[i][0] & mask_list[j][0] == 0:
                    max_prod = max(max_prod, mask_list[i][1] * mask_list[j][1])
        return max_prod
