def average_grades(self):
    aver_grades = 0
    step = 0
    for values_list in self.grades.values():
        for values in values_list:
            aver_grades += int(values)
            step += 1
    aver_grades /= step
    return round(aver_grades, 1)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, self1):
        return average_grades(self) < average_grades(self1)


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_grades(self)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершеные курсы: {", ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, self1):
        return average_grades(self) < average_grades(self1)


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grades(self)}\n'
        return res


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


best_student = Student('Ruoy', 'Eman', 'Man')
best_student.courses_in_progress += ['Python', 'JS']

worse_student = Student('Jon', 'Carter', 'Man')
worse_student.courses_in_progress += ['Python', 'JS']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'JS']
sucks_lecturer = Lecturer('Piter', 'Blad')
sucks_lecturer.courses_attached += ['Python', 'JS']


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor.rate_hw(best_student, 'Python', 5)

cool_mentor.rate_hw(worse_student, 'Python', 3)
cool_mentor.rate_hw(worse_student, 'Python', 2)
cool_mentor.rate_hw(worse_student, 'Python', 4)

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'JS', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
worse_student.rate_lecture(sucks_lecturer, 'Python', 3)
worse_student.rate_lecture(sucks_lecturer, 'JS', 2)
worse_student.rate_lecture(sucks_lecturer, 'Python', 1)

print(best_student.grades)
print(cool_lecturer.grades)
print(best_student)
print(cool_mentor)
print(cool_lecturer)
print(average_grades(best_student))
print(average_grades(worse_student))

print(worse_student < best_student)
print(sucks_lecturer < cool_lecturer)