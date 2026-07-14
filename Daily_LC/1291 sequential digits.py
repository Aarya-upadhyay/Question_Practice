class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        ans="123456789"
        l_c=0
        l=low
        h=high
        h_c=0
        while l:
            d=l%10
            l_c+=1
            
            l//=10
            
        while h:
            d=h%10
            h_c+=1
            h//=10
       
        while l_c<=h_c:
            
            for i in range(len(ans)):
                if i+l_c<=len(ans):
                    a=ans[i:i+l_c]
                    if int(a)>=low and int(a)<=high:
                        res.append(int(a))
                    
            l_c+=1
        return res
