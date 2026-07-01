class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        s=[]
        ans=[0]*len(temp)
        for i in range(len(temp)):
            #if today warmer then prev
            while s and temp[i]>temp[s[-1]]:
                prev=s.pop()
                #how many days wait
                ans[prev]=i-prev
            s.append(i)#today also waits for warmer day
        return ans


        