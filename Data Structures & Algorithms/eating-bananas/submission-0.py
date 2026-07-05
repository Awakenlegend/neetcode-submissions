class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 #min speed
        r=max(piles) #max speed
        ans=r #intially ans is max
        while l<=r:
            mid=(l+r)//2 #eating speed
            hr=0
            #cal total hr for these speed
            for p in piles:
                hr+=(p+mid-1)//mid #round up values 
            #these speed works
            if hr<=h:
                ans=mid #best ans
                r=mid-1 #try slower ans
            #too slow
            else:
                l=mid+1 #need fast 
        return ans

        