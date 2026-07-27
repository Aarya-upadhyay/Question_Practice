class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        def ispalindrome(st):
            return st==st[::-1]

        def backtrack(temp,start):
            if start==len(s):
                ans.append(temp.copy())
                return
            
            for i in range(start,n):
                str1=s[start:i+1]
                if ispalindrome(str1):
                    temp.append(str1)
                    backtrack(temp,i+1)
                    temp.pop()
        backtrack([],0)
        return ans
        
