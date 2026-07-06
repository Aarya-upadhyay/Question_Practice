class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        def speed1(piles,n,speed):
            h1=0
            for i in range(len(piles)):
                h1+=piles[i]//speed
                if piles[i]%speed!=0:
                    h1+=1
            return h1
        low=1
        high=max(piles)
        res=-1
        while low<=high:
            mid=(low+high)//2
            hour=speed1(piles,len(piles),mid)
            if hour>h:
                low=mid+1
            else:
                res=mid
                high=mid-1
        return res
        
        
