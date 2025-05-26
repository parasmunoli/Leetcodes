class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        res=0
        for i in range(l):
            curr=""
            l1=0
            while s[i] not in curr:
                curr+=s[i]
                l1+=1
                i+=1
                if i==l:
                    break
            res=max(res,l1)
        return res