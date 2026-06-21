class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        min_p=pr[0]
        bp=0
        for p in pr:
            min_p=min(p,min_p)
            profit=p-min_p
            bp=max(bp,profit)
        return bp

        