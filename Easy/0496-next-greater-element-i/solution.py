class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        r={}
        for i in range(len(nums2)):
            while res and nums2[i]>nums2[res[-1]]:
                r[nums2[res[-1]]] = nums2[i]
                res.pop()
            res.append(i)
        for i in res:
            r[nums2[i]]=-1
        k=[]
        for i in nums1:
            k.append(r.get(i))
        return k
