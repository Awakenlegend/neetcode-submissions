class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        l=0
        b=0
        mf=0
        for i in range(len(s)):
            c[s[i]]=c.get(s[i],0)+1
            mf=max(mf,c[s[i]])
            while (i-l+1) - mf >k:
               c[s[l]]-=1
               l+=1
            b=max(b,i-l+1)
        return b
