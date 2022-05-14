students_list = []
lecturers_list = []

class Person():
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_avarage(self):
        if self.grades:
            tmp = []
            for value in self.grades.values():
                tmp.extend(value)
            return format(sum(tmp) / len(tmp), ',.1f')
        else:
            return None

    def __str__(self):
        return f'Имя: {self.name}'\
            f'\nФамилия: {self.surname}'\
            f'\nДолжность: {self.position}'\

class Student(Person):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_cw(self, lecturer, course,  grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('No students')
            return
        return float(self.get_avarage()) < float(other.get_avarage())

    def __str__(self):
        return f'Имя: {self.name}'\
            f'\nФамилия: {self.surname}'\
            f'\nДолжность: {self.position}'\
            f'\nЗавершрнные курсы: {", ".join(self.finished_courses)}'\
            f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'\
            f'\nСредняя оценка за домашние задания: {self.get_avarage()}'
    
class Lecturer(Person):
    def __init__(self, name, surname, position,):
        super().__init__(name, surname, position)
        lecturers_list.append(self)
        self.courses_attached = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not Reviuers.')
            return
        return float(self.get_avarage()) < float(other.get_avarage())

    def __str__(self):
        return f'Имя: {self.name}'\
            f'\nФамилия: {self.surname}'\
            f'\nДолжность: {self.position}'\
            f'\nСредняя оценка за лекции: {self.get_avarage()}'
             
class Reviuer(Person):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        return f'Имя: {self.name}'\
            f'\nФамилия: {self.surname}'\
            f'\nДолжность: {self.position}'

def students_avarage(course, students):
    tmp = []
    for student in students:
        if course in student.grades:
            tmp.extend(student.grades[course])
    return format(sum(tmp) / len(tmp), ',.1f')

def lecturers_avarage(course, lecturers):
    tmp = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            tmp.extend(lecturer.grades[course])
    return format(sum(tmp) / len(tmp), ',.1f')

student_1 = Student('Иван', 'Иванов', 'Student')
student_2 = Student('Петр', 'Петров', 'Student')
lecturer_1 = Lecturer('Степан', 'Степанов', 'lecturer')
lecturer_2 = Lecturer('Егор', 'Егоров', 'lecturer')
reviuer_1 = Reviuer('Михаил', 'Михайлов', 'Reviuer')
reviuer_2 = Reviuer('Bilbo', 'Baggins', 'Reviuer')

student_1.courses_in_progress += ['Python', 'C++', "JS"]
student_2.courses_in_progress += ['Python', 'C++', "JS"]
lecturer_1.courses_attached += ['Python', 'C++', "JS"]
lecturer_2.courses_attached += ['Python', 'C++', "JS"]
reviuer_1.courses_attached += ['Python', 'C++', "JS"]
reviuer_2.courses_attached += ['Python', 'C++', "JS"]

reviuer_1.rate_hw(student_1, 'Python', 6)
reviuer_1.rate_hw(student_1, 'Python', 3)
reviuer_1.rate_hw(student_1, 'Python', 9)

reviuer_2.rate_hw(student_2, 'Python', 3)
reviuer_2.rate_hw(student_2, 'Python', 2)
reviuer_2.rate_hw(student_2, 'Python', 7)

student_1.rate_cw(lecturer_1, 'Python', 10)
student_1.rate_cw(lecturer_1, 'Python', 7)
student_1.rate_cw(lecturer_1, 'JS', 10)
student_1.rate_cw(lecturer_2, 'Python', 4)
student_1.rate_cw(lecturer_2, 'Python', 7)
student_1.rate_cw(lecturer_2, 'JS', 2)

print(student_1, end='\n\n')
print(lecturer_1, end='\n\n')
print(reviuer_1, end='\n\n')
print(student_1 > student_2, end='\n\n')
print(f'Средняя оценка по курсу "Python"(студенты): {students_avarage("Python", students_list)}', end='\n\n')
print(f'Средняя оценка по курсу "Pythin"(лекторы):{lecturers_avarage("Python", lecturers_list)}', end='\n\n')