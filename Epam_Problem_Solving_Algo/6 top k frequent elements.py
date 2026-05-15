from collections import Counter
import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count element frequencies in O(N) time
    count = Counter(nums)
    
    # Step 2: Push elements into a Max-Heap in O(N) time
    # Store items as (-frequency, unique_element)
    max_heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Extract the top K elements in O(K log N) time
    result = []
    for _ in range(k):
        # pop() always returns the smallest element (-frequency is lowest)
        freq, num = heapq.heappop(max_heap)
        result.append(num)
        
    return result

""" 
Review
Your solution is correct and meets the problem requirements well. Here's an evaluation based on the given criteria:

Correctness (40%)

You correctly:
Count frequencies using Counter.
Build a max-heap using negative frequencies.
Pop exactly k elements from the heap.
This returns the k most frequent elements.
Edge cases like k = 1, nums with a single element, and all elements being unique are handled correctly by the logic.
Frequency Mapping (20%)

count = Counter(nums) efficiently builds a frequency map in O(n).
It correctly handles duplicates and unique elements.
Heap Usage (20%)

You use a max-heap pattern by pushing (-freq, num) into a standard Python min-heap.
heapq.heapify(max_heap) is O(m), where m is the number of unique elements.
Then you pop k times to get the top k frequent elements.
This is a standard and acceptable approach.
Efficiency (10%)

Let m be the number of unique elements.
Building the Counter: O(n).
Building the heap: O(m).
Extracting k elements: O(k log m).
Overall complexity: O(n + m + k log m) ≈ O(n log n) in worst case, which satisfies the constraints.
Space complexity is O(m) for the Counter and heap, proportional to the number of unique elements.
Code Quality (10%)

Readable and idiomatic Python.
Good use of standard library (Counter, heapq).
Type hints are present (List[int]).
Comments explain each step clearly."""
