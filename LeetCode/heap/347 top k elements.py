class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        heap=[]
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        # Step 3
        ans = []

        for _ in range(k):
            count, num = heapq.heappop(heap)
            ans.append(num)

        return ans



        
        
