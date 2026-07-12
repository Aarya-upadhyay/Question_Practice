class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        ranks={val:i+1 for i,val in enumerate(arr)}
        for i in range(len(arr)):
            arr[i]=ranks[arr[i]]
        return arr
        
