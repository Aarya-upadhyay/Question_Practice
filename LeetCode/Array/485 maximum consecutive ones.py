class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        co=0
        maxi=0
        for i in nums:
            if i==1:
                co+=1
                maxi=max(maxi,co)
            else:
                co=0
        return maxi

        
