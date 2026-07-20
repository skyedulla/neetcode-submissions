from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        unavailable_courses = defaultdict(set)
        available_courses = set()

        for i in range(numCourses):
            available_courses.add(i)

        for course, prerequisite in prerequisites:
            unavailable_courses[course].add(prerequisite)
            if course in available_courses:
                available_courses.remove(course)

        
        possible_course_order = list(available_courses)

        unlocked_courses = []
        unlocking_courses = True
        while unlocking_courses and len(unavailable_courses) >= 0:
            unlocking_courses = False
            for course, prereqs in unavailable_courses.items():
                if prereqs.issubset(available_courses):
                    unlocked_courses.append(course)
                    available_courses.add(course)
                    unlocking_courses = True
                
            for course in unlocked_courses:
                del unavailable_courses[course]

            possible_course_order += unlocked_courses
            unlocked_courses = []
        
        if len(unavailable_courses) > 0:
            return []
        else:
            return possible_course_order

