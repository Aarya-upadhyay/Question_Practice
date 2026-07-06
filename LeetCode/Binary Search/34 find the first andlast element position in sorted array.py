class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first(nums, target):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1      # keep searching left

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        def last(nums, target):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1       # keep searching right

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        return [first(nums, target), last(nums, target)]
