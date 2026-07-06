class Solution:
    def countFreq(self, arr, target):

        def first(arr, target):
            l = 0
            h = len(arr) - 1
            first = -1

            while l <= h:
                mid = (l + h) // 2

                if arr[mid] < target:
                    l = mid + 1

                elif arr[mid] > target:
                    h = mid - 1

                else:
                    first = mid
                    h = mid - 1

            return first

        def last(arr, target):
            l = 0
            h = len(arr) - 1
            last = -1

            while l <= h:
                mid = (l + h) // 2

                if arr[mid] < target:
                    l = mid + 1

                elif arr[mid] > target:
                    h = mid - 1

                else:
                    last = mid
                    l = mid + 1

            return last

        f = first(arr, target)

        if f == -1:
            return 0

        l = last(arr, target)

        return l - f + 1
