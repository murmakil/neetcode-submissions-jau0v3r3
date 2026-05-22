from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while len(students) > 0:
            current = students.copy()
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft() 
            else:
                x = students.popleft()
                students.append(x)
            if students == current:
                return len(students)
        return 0  