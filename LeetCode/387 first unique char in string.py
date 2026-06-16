class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx=-1
        h={}
        for i in range(len(s)):
            h[s[i]]=h.get(s[i],0)+1
        for i in range(len(s)):
            if h[s[i]]==1:
                return i
        return idx

                
