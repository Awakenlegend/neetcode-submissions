class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force O(n*2)
        #res=[]
        # for i in range(len(nums)):
        #     p=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             p*=nums[j]
        #     res.append(p)
        # return res
        n=len(nums)
        ans=[1]*n
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        r=1
        for i in range(n-1,-1,-1):
            ans[i]*=r
            r*=nums[i]
        return ans