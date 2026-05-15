class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        res=[]
        def back(curr,open_par,close_par):
            if len(curr)==n*2:
                res.append(curr)
                return
            if open_par<n:

                back(curr+"(",open_par+1,close_par)
            if close_par<open_par:
                back(curr+")",open_par,close_par+1)
        back("",0,0)
        return res
        
