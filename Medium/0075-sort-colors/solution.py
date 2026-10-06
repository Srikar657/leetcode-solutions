class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=mid=high=0
        for i in nums:
            if i == 0:
                low+=1
            elif i == 1:
                mid+=1
            elif i == 2:
                high+=1
        count =0
        for i in range(len(nums)):
            if count<low:
                nums[i]=0
            elif count < low+mid:
                nums[i]=1
            else:
                nums[i]=2
            count+=1
