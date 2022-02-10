class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lct(self, lecture, course, grade):
        if isinstance(lecture, (Lecturer, Reviewer)) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grade_middle(self):
        grades_cnt = 0
        grade_md = 0
        for course, grades in self.grades.items():
            for grade in grades:
                grade_md += grade
                grades_cnt += 1
        if grades_cnt > 0:
            grade_md = round(grade_md / grades_cnt , 1)
        return grade_md

    def __str__(self):
        new_line = '\n'
        grade_md = self.grade_middle()
        courses_in_progress = ', '.join([str(course) for course in self.courses_in_progress])
        finished_courses = ', '.join([str(course) for course in self.finished_courses])
        res = f"Имя: {self.name}{new_line}Фамилия: {self.surname}{new_line}Средняя оценка за лекции: {grade_md}{new_line}Курсы в процессе изучения: {courses_in_progress}{new_line}Завершнные курсы: {finished_courses}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Один из операндов не является экземпляром класса Student")
        else:
            return self.grade_middle() < other.grade_middle()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def grade_middle(self):
        grades_cnt = 0
        grade_md = 0
        for course, grades in self.grades.items():
            for grade in grades:
                grade_md += grade
                grades_cnt += 1
        if grades_cnt > 0:
            grade_md = round(grade_md / grades_cnt , 1)
        return grade_md

    def __str__(self):
        new_line = '\n'
        grade_md = self.grade_middle()
        res = f"Имя: {self.name}{new_line}Фамилия: {self.surname}{new_line}Средняя оценка за лекции: {grade_md}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Один из операндов не является экземпляром класса Lecturer")
        else:
            return self.grade_middle() < other.grade_middle()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        new_line = '\n'
        res = f"Имя: {self.name}{new_line}Фамилия: {self.surname}"
        return res

def students_middle_rate(students, course):
    grades_cnt = 0
    grade_md = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for grade in student.grades[course]:
                grade_md += grade
                grades_cnt += 1
        else:
            return 'Ошибка'
    if grades_cnt > 0:
        grade_md = round(grade_md / grades_cnt, 1)
    return grade_md

def lecturers_middle_rate(lecturers, course):
    grades_cnt = 0
    grade_md = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                grade_md += grade
                grades_cnt += 1
        else:
            return 'Ошибка'
    if grades_cnt > 0:
        grade_md = round(grade_md / grades_cnt, 1)
    return grade_md

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Java', 'C#']
best_student.finished_courses += ['Кройки и шитья', '3D-моделирования']

other_student = Student('John', 'Smith', 'apache')
other_student.courses_in_progress += ['Python', 'Java', 'C#']
other_student.finished_courses += ['Нарезки ролов', 'Починки жигулей']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

hot_mentor = Reviewer('Any', 'One')
hot_mentor.courses_attached += ['Java']

first_lecturer = Lecturer('First', 'Lector')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Js']

second_lecturer = Lecturer('Second', 'Lector')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 7)
hot_mentor.rate_hw(best_student, 'Java', 8)
hot_mentor.rate_hw(best_student, 'Java', 9)
hot_mentor.rate_hw(best_student, 'Java', 7)
hot_mentor.rate_hw(best_student, 'Java', 7)

cool_mentor.rate_hw(other_student, 'Python', 10)
cool_mentor.rate_hw(other_student, 'Python', 9)
cool_mentor.rate_hw(other_student, 'Python', 8)
hot_mentor.rate_hw(other_student, 'Java', 10)
hot_mentor.rate_hw(other_student, 'Java', 9)
hot_mentor.rate_hw(other_student, 'Java', 10)
hot_mentor.rate_hw(other_student, 'Java', 7)

best_student.rate_lct(first_lecturer, 'Python', 10)
other_student.rate_lct(first_lecturer, 'Python', 10)
best_student.rate_lct(first_lecturer, 'Java', 9)

other_student.rate_lct(second_lecturer, 'Python', 10)
best_student.rate_lct(second_lecturer, 'Python', 7)
other_student.rate_lct(second_lecturer, 'Java', 6)

students_list = [best_student, other_student]
lecturers_list = [first_lecturer, second_lecturer]

print('Менторы')
print(cool_mentor)
print(hot_mentor)
print('Лекторы')
print(first_lecturer)
print(second_lecturer)
print('Студенты')
print(best_student)
print(other_student)

print('Сравнение лекторов')
print(first_lecturer > second_lecturer)
print('Сравнение студентов')
print(best_student > other_student)

print('Средня оценка студентов по курсу Python')
print(students_middle_rate(students_list, 'Python'))

print('Средня оценка лекторов по курсу Python')
print(lecturers_middle_rate(lecturers_list, 'Python'))
