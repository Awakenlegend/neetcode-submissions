class Solution:
    def largestRectangleArea(self, hi: List[int]) -> int:

        s = []  #to store i and h
        maxans = 0  #we need to return max area

        for i, h in enumerate(hi):

            st = i  #curr building start here

            #short building arrived
            while s and s[-1][1] > h:

                ind, height = s.pop()

                #cal max area
                maxans = max(maxans, height * (i - ind))

                #current building goes left bcz its small
                st = ind

            s.append((st, h))  #building waiting for small

        #building didn't find small
        for ind, height in s:

            maxans = max(maxans, height * (len(hi) - ind))

        return maxans