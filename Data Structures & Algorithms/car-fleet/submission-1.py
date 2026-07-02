class Solution:
    def carFleet(self, t: int, pos: List[int], s: List[int]) -> int:
        cars = list(zip(pos, s))  #combine pos with there speed
        cars.sort()  #we need this to know which reaches fisrt

        stack = []  #to store fleet time

        #from nearest car to target
        for p, speed in cars[::-1]:

            #time to reach the tar
            time = (t - p) / speed

            #new fleet
            stack.append(time)

            #join previous and compare fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  #bcz behind car can catch the front car they bcome same fleet

        return len(stack)