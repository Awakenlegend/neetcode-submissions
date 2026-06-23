class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        h=Counter(s1)
        w=Counter(s2[:len(s1)])
        if h==w:
            return True
        l=0
        for i in range(len(s1),len(s2)):
            w[s2[i]]+=1
            w[s2[l]]-=1
            if w[s2[l]]==0:
                del w[s2[l]]
            l+=1
            if h==w:
                return True
        return False


        