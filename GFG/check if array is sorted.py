class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        """a=arr.copy()
        a.sort()
        if arr==a:
            return True
        else:
            return False
        # o(n log n)
        """
        """ for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True
        # O(n)
        
        """
        if len(arr)<=1:
            return True
        if arr[-2]>arr[-1]:
            return False
        return self.isSorted(arr[:-1])
        
        
            
        
