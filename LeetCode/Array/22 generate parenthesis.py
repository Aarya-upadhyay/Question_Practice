class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(curr,open_b,close_b):
            if len(curr)==2*n:
                ans.append(curr)
                return
            if open_b<n:
                backtrack(curr+"(",open_b+1,close_b)
            if close_b<open_b:
                backtrack(curr+")",open_b,close_b+1)
        backtrack("",0,0)
        return ans
        
