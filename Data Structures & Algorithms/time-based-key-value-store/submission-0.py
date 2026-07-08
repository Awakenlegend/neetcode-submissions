class TimeMap:

    def __init__(self):
        self.store={}#store key and val 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #first if u see key
        if key not in self.store:
            self.store[key]=[]
        #timestamps are increasing so just append
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        #key doesn't exist
        if key not in self.store:
            return ""
        arr=self.store[key] #list of timestamp and val
        l=0
        r=len(arr)-1
        ans=""#best timestamp so for
        while l<=r:
            mid=(l+r)//2
            #curr timesatmp is valid
            if arr[mid][0]<=timestamp:
                ans=arr[mid][1]#save curr best val
                #may larger ts exist
                l=mid+1
            #ts is too large
            else:
                r=mid-1
        return ans
        
