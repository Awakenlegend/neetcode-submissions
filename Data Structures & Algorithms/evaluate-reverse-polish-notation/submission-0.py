class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for t in tokens:
            if t not in ['+','-','*','/']:
                s.append(int(t))
            else:
                r=s.pop()#last ele
                l=s.pop()#last sec ele
                if t=='+':
                    s.append(l+r)
                elif t=='-':
                    s.append(l-r)
                elif t=='*':
                    s.append(l*r)
                elif t=='/':
                    s.append(int(l/r))
        return s[-1]



        