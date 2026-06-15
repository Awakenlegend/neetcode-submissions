class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in g:
                g[key]=[]
            g[key].append(s)
        return list(g.values())#tc=O(n*klogk) sc=O(n*k)
        