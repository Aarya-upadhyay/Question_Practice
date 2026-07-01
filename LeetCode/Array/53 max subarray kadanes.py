class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            a1=best+nums[i]
            a2=nums[i]
            best=max(a1,a2)
            ans=max(ans,best)
        return ans
