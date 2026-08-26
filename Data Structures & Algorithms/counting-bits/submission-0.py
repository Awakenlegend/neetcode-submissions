class Solution:
    def countBits(self, n: int) -> List[int]:
        of=1
        dp=[0]*(n+1)
        for i in range(1,n+1):
            if of*2==i:
                of=i
            dp[i]=1+dp[i-of]
        return dp
        