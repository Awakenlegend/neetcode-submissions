class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        b=0
        while l<r:
            a=min(h[l],h[r])*(r-l)
            b=max(a,b)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return b
