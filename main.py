from logging_module import logger
from models import Human, Student, Group


# создаем 10 студентов
student1 = Student('Yarik', 28, 'male', 'biofac', 1)
student2 = Student('Vasya', 18, 'male', 'mathfac', 2)
student3 = Student('Mohammed', 38, 'male', 'IT', 3)
student4 = Student('Joe', 20, 'male', 'literature', 4)
student5 = Student('Anastasia', 20, 'female', 'kosmo', 5)
student6 = Student('Olga', 19, 'female', 'biofac', 5)
student7 = Student('Yurik', 23, 'male', 'mathfac', 4)
student8 = Student('Kostian', 24, 'male', 'IT', 3)
student9 = Student('Ronald', 26, 'male', 'biofac', 2)
student10 = Student('Patrik', 28, 'male', 'literature', 1)
student11 = Student('Natasha', 50, 'female', 'math', 3)

# Добавляем/убираем студентов группы
group_1 = Group()

group_1.add_student(student1)
group_1.add_student(student2)
group_1.add_student(student3)
group_1.add_student(student4)
group_1.add_student(student5)
group_1.add_student(student6)
group_1.add_student(student7)
group_1.add_student(student8)
group_1.add_student(student9)
group_1.add_student(student10)
# group_1.add_student(student11)


# group_1.del_student(student1)
# group_1.del_student(student2)

print('*' * 35)
print(group_1)
print()
# список студентов
grp_list = group_1.get_student_list()
print(grp_list)

# проверка есть ли студент в группу
ifStudentInGroup = group_1.find_student('Poroshenko')
print('Student in group' if ifStudentInGroup else 'Student not found')
