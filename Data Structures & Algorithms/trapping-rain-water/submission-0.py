class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        ans=0
        r=len(h)-1
        lm=h[l]
        rm=h[r]
        while l<r:
            if lm < rm:
                l+=1
                lm=max(lm,h[l])
                ans+=lm-h[l]
            else:
                r-=1
                rm=max(rm,h[r])
                ans+=rm-h[r]
        return ans
