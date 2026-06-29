class Solution:
    def isValid(self, s: str) -> bool:

        stack = []  #store opening locks

        h = {
            ')': '(',
            ']': '[',
            '}': '{'
        }  #closing key -> opening lock

        for c in s:

            #opening lock
            if c not in h:
                stack.append(c)

            #closing key
            else:

                #no lock or wrong lock
                if not stack or stack[-1] != h[c]:
                    return False

                #correct lock found
                stack.pop()

        #all locks should be opened
        return len(stack) == 0