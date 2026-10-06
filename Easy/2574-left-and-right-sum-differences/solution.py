class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total=sum(nums)
        leftsum=0
        answer=[0]*len(nums)
        for i in range(len(nums)):
            rightsum=total-leftsum-nums[i]
            answer[i]=abs(leftsum-rightsum)
            leftsum+=nums[i]
        return answer
