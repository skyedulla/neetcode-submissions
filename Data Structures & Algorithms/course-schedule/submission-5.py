from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #The prerequistes array represents a set of rules for taking a course. We have to scan this
        #array and ensure there are no closes loops or required courses that are greater than 0 or
        locked_courses = defaultdict(set)
        unlocked_courses = set()

        for i in range(0, numCourses):
            unlocked_courses.add(i)


        for prereq in prerequisites:
            if prereq[1] >= numCourses or prereq[1] < 0:
                return False

            if prereq[0] in unlocked_courses:
                unlocked_courses.remove(prereq[0])
            locked_courses[prereq[0]].add(prereq[1])
        

        remove_courses = []
        course_unlocked = True
        while len(locked_courses) > 0 and course_unlocked:
            course_unlocked = False
            for course, prereqs in locked_courses.items():
                if prereqs.issubset(unlocked_courses):
                    unlocked_courses.add(course)
                    remove_courses.append(course)
                    course_unlocked = True

            for course in remove_courses:
                del locked_courses[course]
            remove_courses = []




        if len(locked_courses) > 0:
            return False
        else:
            return True
            
           
                
                

        #Now that we have a list of all the courses we need verify can be taken if we complete
        #all the available courses we can create a loop that loops through all the locked courses
        #and check if the prereq key is in unlocked courses.
        #we can repeat this loop until one full iteration unlocks 0 courses or until locked_courses is empty