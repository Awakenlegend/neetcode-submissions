class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        g=set()
        l=0
        b=0
        for i in range(len(s)):
            while s[i] in g:
                g.remove(s[l])
                l+=1
            g.add(s[i])
            b=max(b,i-l+1)
        return b

        