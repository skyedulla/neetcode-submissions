from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """we insert elements into a deque in decreasing order and after every 
        insertion we pop all elements left of the insertion"""
        answer = []
        q = deque()
        for R in range(len(nums)):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
                
            q.append(R)
            
            if q[0] < R - k + 1:
                q.popleft()

            if R >= k - 1:
                answer.append(nums[q[0]])
                

        return answer