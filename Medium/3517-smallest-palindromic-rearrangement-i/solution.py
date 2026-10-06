class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        chars=sorted(freq.keys())
        first_half=[]
        middle=""
        for ch in chars:
            count=freq[ch]
            first_half.append(ch*(count//2))
            if count%2==1:
                middle=ch
        first_half_str="".join(first_half)
        return first_half_str+middle+first_half_str[::-1]
