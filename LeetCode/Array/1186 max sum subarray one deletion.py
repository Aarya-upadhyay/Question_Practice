class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        keep = arr[0]
        delete = 0

        ans = arr[0]

        for i in range(1, len(arr)):

            new_delete = max(delete + arr[i], keep)

            new_keep = max(arr[i], keep + arr[i])

            keep = new_keep
            delete = new_delete

            ans = max(ans, keep, delete)

        return ans
