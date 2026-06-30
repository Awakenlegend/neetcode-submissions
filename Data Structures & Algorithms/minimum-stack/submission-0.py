class MinStack:

    def __init__(self):
        self.stack=[]#main tre
        self.minstack=[]#cap notebook
        

    def push(self, val: int) -> None:
        self.stack.append(val)#adding val
        #adding to cap notebook
        if not self.minstack:
            self.minstack.append(val)
        else:
            #comapre with main and cap
            self.minstack.append(min(val,self.minstack[-1]))
        
    def pop(self) -> None:
        #remove main tre
        self.stack.pop()
        #remove cap
        self.minstack.pop()
        
    def top(self) -> int:
        #top tre
        return self.stack[-1]

    def getMin(self) -> int:
        #smallest tre
        return self.minstack[-1]
        
