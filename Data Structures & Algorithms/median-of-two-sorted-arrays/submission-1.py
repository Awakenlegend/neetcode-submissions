class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #always bs on smaller array
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        A=nums1
        B=nums2
        total=len(A) + len(B)
        leftsize=(total+1)//2
        l=0
        r=len(A)
        while l<=r:
             # Number of elements taken from A
            i=(l+r)//2
            # Number of elements taken from B
            j=leftsize-i
            # Border values around the knife
            L1 = A[i-1] if i > 0 else float("-inf")
            R1 = A[i] if i < len(A) else float("inf")

            L2 = B[j-1] if j > 0 else float("-inf")
            R2 = B[j] if j < len(B) else float("inf")
            # Correct partition found
            if L1 <= R2 and L2 <= R1:

                # Odd total elements
                if total % 2:
                    return max(L1, L2)

                # Even total elements
                return (max(L1, L2) + min(R1, R2)) / 2
            # Too mnay elements from A
            elif L1>R2:
                r=i-1
            #Too few elements from A
            else:
                l=i+1

           
        