class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            cap=nums[i]
            t=-cap
            l=i+1
            r=len(nums)-1
            while l<r:
                can=nums[l]+nums[r]
                if can==t:
                    ans.append([cap,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif can<t:
                    l+=1
                else:
                    r-=1
                    
        return ans