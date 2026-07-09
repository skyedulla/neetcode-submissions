from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """we insert elements into a deque in decreasing order and after every 
        insertion we pop all elements left of the insertion"""
        answer = []
        q = deque()
        heap = []
        for R in range(len(nums)):
            while heap and heap[0][1] < R - k + 1:
                heapq.heappop(heap)
                
            heapq.heappush(heap, [-nums[R], R])
            
            if R >= k - 1:
                answer.append(-heap[0][0])
                

        return answer