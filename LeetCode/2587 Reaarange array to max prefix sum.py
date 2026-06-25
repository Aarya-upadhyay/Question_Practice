class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c=0
        """prefix=[0]*len(nums)
        prefix[0]=nums[0]
        if prefix[0]>0:
            c+=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
            if prefix[i]>0:
                c+=1
        return c"""
        run_sum=0
        for i in nums:
            run_sum+=i
            if run_sum>0:
                c+=1
        return c


        
