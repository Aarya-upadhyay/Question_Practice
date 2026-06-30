class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]>=2:
                return i"""
        
        #slow and fast pointers ho skta hai 
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
            if slow==fast:
                slow=0
                while slow!=fast:
                    slow=nums[slow]
                    fast=nums[fast]
                return slow
        return -1
        
        
