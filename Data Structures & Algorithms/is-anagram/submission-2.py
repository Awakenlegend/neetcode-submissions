from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      #brute force 
      '''if sorted(s) == sorted(t):
            return True
        else:
            return False '''
      #optimal solution
      return Counter(s)==Counter(t)