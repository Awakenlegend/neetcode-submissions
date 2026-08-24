class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        res=[0]*n
        res_idx=n-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[res_idx]=nums[l]*nums[l]
                l+=1
            else:
                res[res_idx]=nums[r]*nums[r]
                r-=1
            res_idx-=1
        return res
            
        