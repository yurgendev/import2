from logging_module import logger

class MaxStdInGroup(Exception):
    pass


class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Basic example of a human may be presented as a name{self.name}, age{self.age} and its gender{self.gender}"


class Student(Human):

    def __init__(self, name, age, gender, faculty, course):
        super().__init__(name, age, gender)
        self.faculty = faculty
        self.course = course

    def __str__(self):
        return f"Welcome our student - {self.name}. He is {self.age} y.o. and {self.gender} gender. " \
               f"This year student enrolled in {self.faculty} on {self.course} course!"


class Group():

    def __init__(self, students=None, max_students=10):
        if students is None:
            students = []
        self.students = students
        self.max_students = max_students

    def __str__(self):
        return f"This group consists of {len(self.students)} students"

    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
            logger.info(f"Student {student.name} has been added to {student.faculty} on the {student.course}course")
        if len(self.students) > self.max_students:
            raise MaxStdInGroup('there can be no more than 10 students in a group')



    def del_student(self, student):
        if student in self.students:
            self.students.remove(student)
            logger.info(f"Student {student.name} has been deleted")

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def get_student_list(self):
        student_list = ""
        for student in self.students:
            student_list += str(student) + "\n"
        return student_list