class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      

        #optimal sol
        g={}
        for s in strs:
            freq=[0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            key=tuple(freq)
            if key not in g:
                g[key]=[]
            g[key].append(s)
        return list(g.values())
         # brute force
        # g={}
        #for s in strs:
         #   key=''.join(sorted(s))
          #  if key not in g:
           #     g[key]=[]
            #g[key].append(s)
        #return list(g.values())#tc=O(n*klogk) sc=O(n*k)'''
        