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
        res = f"Имя: {self.name}{new_line}Фамилия: {self.surname}{new_line}Средняя оценка за лекции: {grade_md}{new_line}Курсы в процессе изучения: {new_line}Завершнные курсы: {str(self.finished_courses)}"
        return res

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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Js']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

first_lecturer = Lecturer('First', 'Lector')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Js']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 7)

best_student.rate_lct(first_lecturer, 'Python', 10)
best_student.rate_lct(first_lecturer, 'Python', 8)
best_student.rate_lct(first_lecturer, 'Js', 9)

print(first_lecturer)
print(first_lecturer.grades)
print(best_student)
print(best_student.grades)
