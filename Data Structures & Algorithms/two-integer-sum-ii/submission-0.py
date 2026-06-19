class Solution:
    def twoSum(self, num: List[int], t: int) -> List[int]:
        l=0
        r=len(num)-1
        while l<r:
            c=num[l]+num[r]
            if c==t:
                return [l+1,r+1]
            if c<t:
                l+=1
            if c>t:
                r-=1
            
        