from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while queue:
            course_in_progress = queue.popleft()
            order.append(course_in_progress)
            
            for val in adj[course_in_progress]:
                in_degree[val] -= 1
                if in_degree[val] == 0:
                    queue.append(val)


        return order if len(order) == numCourses else []

