import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we flip sign on numbers to make it a max heap
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums) 

        self.heap = nums
        self.k = k

        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val) 
        
        return heapq.nsmallest(self.k, self.heap)[-1] * -1
        
