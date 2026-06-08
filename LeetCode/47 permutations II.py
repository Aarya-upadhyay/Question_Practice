class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                if path not in res:
                    res.append(path[:])
                    return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                backtrack(path)
                path.pop()
                used[i]=False
        backtrack([])
        return res
    """ its not optimal because i have  put condition on the way where i have added to main answer list """
 """" Following is the optimal"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        used=[False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i]=True
                backtrack(path)
                path.pop()
                used[i]=False
        backtrack([])
        return res
