import heapq

def get_k_smallest(nums, k):
    # Build a min-heap from all elements in O(n)
    heapq.heapify(nums)

    # Extract the k smallest elements
    result = []
    for _ in range(k):
        result.append(heapq.heappop(nums))

    # result is already in ascending order because we repeatedly pop the min
    return result
""" Review
Uses heapq.heapify(nums) as requested.
Uses heapq.heappop() k times to extract the smallest elements.
Time complexity: O(n + k log n).
Returns k smallest elements in ascending order, matching the examples.
Overall Grade
Correctness: 0/40
Min-Heap Usage: 15/25
Efficiency: 15/15
Code Quality: 8/10
Edge Cases & Constraints: 5/10
Total: 43/100

To fully meet the task requirements, adjust the goal from "k largest" to "k smallest" and follow the heapify + k heappops pattern shown above.
"""
