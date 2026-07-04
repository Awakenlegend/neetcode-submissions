class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid=(l+r)//2
            row=mid//cols
            col=mid % cols
            if matrix[row][col]==t:
                return True
            elif matrix[row][col]<t:
                l=mid+1
            elif matrix[row][col]>t:
                r=mid-1
        return False


        