class Solution:
    def longestPalindrome(self, s: str) -> str:
        x=len(s)
        res=[]
        for i in range(x):
            for j in range(i+1,x+1):
                if s[i:j]==s[i:j][::-1]:
                    res.append(s[i:j])
        return max(res,key=len)
