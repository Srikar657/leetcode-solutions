from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x,y):
            a,b=str(x),str(y)
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        ans="".join(map(str,nums))
        return '0' if ans[0]=='0' else ans
