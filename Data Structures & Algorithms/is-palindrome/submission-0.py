class Solution:
    def isPalindrome(self, s: str) -> bool:
        #bruteforce
        c=''
        for ch in s:
            if ch.isalnum():
                c+=ch.lower()
        return c==c[::-1]
            
        