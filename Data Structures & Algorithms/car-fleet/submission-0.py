class Solution:
    def carFleet(self, t: int, pos: List[int], sp: List[int]) -> int:
        cars=list(zip(pos,sp))#combine pos with there speed
        cars.sort()#we need this to know which reaches fisrt
        s=[]#to store fleet time
        #from nearest car to target
        for p,sp in cars[::-1]:
            #time to reach the tar
            time=(t-p)/sp
            #new fleet
            s.append(time)
            #join previous and compare fleet
            if len(s)>=2 and s[-1]<=s[-2]:
                s.pop()#bcz behind car can catch the front car they bcome same fleet
        return len(s)
        