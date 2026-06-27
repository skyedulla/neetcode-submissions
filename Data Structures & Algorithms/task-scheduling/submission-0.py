import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_occurences = {}
        max_heap = []

        for task in tasks:
            if task in task_occurences:
                task_occurences[task] += 1
            else:
                task_occurences[task] = 1
        
        for frequency in task_occurences.values():
            heapq.heappush(max_heap, -frequency)
        
        cycles = 0
        dequ = deque()
        while len(max_heap) > 0 or any(dequ):
            if len(max_heap) > 0:
                task = heapq.heappop(max_heap)
                task += 1

                if task < 0:
                    dequ.append(task)
                else:
                    dequ.append(None)
            else:
                dequ.append(None)

            if len(dequ) > n:
                ready_task = dequ.popleft()
                if ready_task:
                    heapq.heappush(max_heap, ready_task)
            
                
                    
            cycles += 1


        return cycles
