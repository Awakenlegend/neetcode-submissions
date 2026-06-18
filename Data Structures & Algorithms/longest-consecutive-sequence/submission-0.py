class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        l_s=0
        for num in nums_set:
            cn=num
            c_s=1
            while cn+1 in nums_set:
                cn+=1
                c_s+=1
            l_s=max(c_s,l_s)
        return l_s
        