import heapq
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        #arr.sort()
        #return arr[k-1]
        heap=[]
        for i in range(k):
            heapq.heappush(heap,-(arr[i]))
        for i in range(k,len(arr)):
            if arr[i]>=-heap[0]:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap,-arr[i])
        return -heap[0]
