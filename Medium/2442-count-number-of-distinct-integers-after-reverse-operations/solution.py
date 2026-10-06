class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in nums:
            n=str(i)
            a.append(int(n[::-1]))
        nums+=a
        return len(set(nums))
