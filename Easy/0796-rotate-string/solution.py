class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(goal)):
            if s == goal[i:]+goal[:i]:
                return True
        return False
