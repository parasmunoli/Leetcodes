class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        ans=-1
        for x,a in enumerate(s):
            for y,b in enumerate(s):
                if a==b and x!=y:
                    ans=max(ans,abs(x-y)-1)
        return ans  