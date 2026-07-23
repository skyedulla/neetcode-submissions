from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for data in times:
            if data[0] not in graph:
                graph[data[0]] = []
            graph[data[0]].append((data[1], data[2]))
            



        #now we have a graph that shows direction. We will use a heap queue to 
        #add connections from the starting node k to all other nodes. We will 
        #prune branches when a node value is popped a a time value has already
        #been calculated or when a new time is calculated and it is more than the
        #one in the time dict

        times = {k: 0}

        heap = [(k, 0)]


        while heap:
            curr, time = heappop(heap)

            if times[curr] < time or curr not in graph:
                continue

        
            for next, ms in graph[curr]:
                time_to_reach_next = time + ms

                if next in times and times[next] <= time_to_reach_next:
                    continue

                heappush(heap, (next, time_to_reach_next))
                times[next] = time_to_reach_next

        
        if len(times) < n:
            return -1 

        min_time = 0
        

        for val in times.values():
            min_time = max(min_time, val)

        return min_time


            