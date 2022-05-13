class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('''Ошибка. Лектор не является экземпляром класса Lecturer и/или студент 
не обучается на данном курсе и/или лектор не проводит лекции на этом курсе.''')

    def __average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for grades_list in self.grades.values():
                count += sum(grades_list) / len(grades_list)
            return round(count / len(self.grades), 1)
        else:
            return 'У студента пока нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.__average_grade()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка. Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() < other.__average_grade()
        return 'У одного или обоих студентов пока нет оценок'

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка. Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() <= other.__average_grade()
        return 'У одного или обоих студентов пока нет оценок'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка. Студентов нужно сравнивать со студентами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() == other.__average_grade()
        return 'У одного или обоих студентов пока нет оценок'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def __average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for grades_list in self.grades.values():
                count += sum(grades_list) / len(grades_list)
            return round(count / len(self.grades), 1)
        else:
            return 'У лектора пока нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка. Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() < other.__average_grade()
        return 'У одного или обоих лекторов пока нет оценок'

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка. Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() <= other.__average_grade()
        return 'У одного или обоих лекторов пока нет оценок'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка. Лекторов нужно сравнивать с лекторами'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.__average_grade() == other.__average_grade()
        return 'У одного или обоих лекторов пока нет оценок'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('''Ошибка. Студент не является экземпляром класса Student и/или студент 
не обучается на данном курсе и/или преподаватель не проверяет задания на этом курсе.''')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


students_list = []
lecturer_list = []

# Инициализируем экземпляры класса, заполняем им списки курсов
ivan = Student('Иван', 'Иванов', 'м')
ivan.courses_in_progress.append('Git')
ivan.courses_in_progress.append('Python')
ivan.finished_courses.append('Английский')

mary = Student('Мария', 'Сидорова', 'ж')
mary.courses_in_progress.append('Git')
mary.courses_in_progress.append('Английский')
mary.finished_courses.append('Python')

git_english_lecturer = Lecturer('Владимир', 'Петров')
git_english_lecturer.courses_attached.append('Git')
git_english_lecturer.courses_attached.append('Английский')

python_lecturer = Lecturer('Тамара', 'Ветрова')
python_lecturer.courses_attached.append('Python')

git_python_reviewer = Reviewer('Анна', 'Азимова')
git_python_reviewer.courses_attached.append('Git')
git_python_reviewer.courses_attached.append('Python')

english_reviewer = Reviewer('Леонард', 'Дубовицкий')
english_reviewer.courses_attached.append('Английский')

# Познакомимся с нашими экспертами по проверке домашних заданий
print(git_python_reviewer)
print(english_reviewer, end='\n\n')

# Теперь вызовем методы выставления оценок студентам
# Эксперт по английскому ставит оценки Маше, все в порядке
english_reviewer.rate_hw(mary, 'Английский', 10)
english_reviewer.rate_hw(mary, 'Английский', 8)
english_reviewer.rate_hw(mary, 'Английский', 9)
print(mary, end='\n\n')

# Эксперт по английскому ставит оценки Ивану. Иван уже закончил курс, оценки не ставятся.
english_reviewer.rate_hw(ivan, 'Английский', 7)
print(ivan, end='\n\n')

# Эксперт по GIT и Python ставит оценки Маше. Маша завершила Python, а эксперт не проверяет английский, 2 ошибки.
git_python_reviewer.rate_hw(mary, 'Git', 6)
git_python_reviewer.rate_hw(mary, 'Git', 8)
git_python_reviewer.rate_hw(mary, 'Python', 8)
git_python_reviewer.rate_hw(mary, 'Английский', 3)
print(mary.grades)
print(mary, end='\n\n')

# Эксперт по Git и Python ставит оценки Ивану. Иван закончил английский, да и эксперт эти дз не проверяет, 1 ошибка
git_python_reviewer.rate_hw(ivan, 'Git', 9)
git_python_reviewer.rate_hw(ivan, 'Git', 7)
git_python_reviewer.rate_hw(ivan, 'Python', 9)
git_python_reviewer.rate_hw(ivan, 'Python', 8)
git_python_reviewer.rate_hw(ivan, 'Python', 3)
git_python_reviewer.rate_hw(ivan, 'Английский', 6)
print(ivan.grades)
print(ivan, end='\n\n')

# Если эксперт попытается оценить эксперта или лектора, получим ошибку
git_python_reviewer.rate_hw(english_reviewer, 'Git', 5)
english_reviewer.rate_hw(python_lecturer, 'Английский', 10)
print()

# Сравним разные экземпляры
# Иван с Машей и Маша с Иваном
print('Иван учится хуже Маши?', ivan < mary)
print('Иван учится хуже или так же, как Маша?', ivan <= mary)
print('Иван учится лучше или так же, как Маша?', ivan >= mary)
print('Маша не так же, как Иван?', mary != ivan)
print('Маша так же, как Иван?', mary == ivan, end='\n\n')

# Ставним студента с лектором и экспертом, получаем ошибку.
print(ivan > python_lecturer)
print(mary < english_reviewer)
# Создадим еще одного студента без оценок, сравним с Иваном
new_student = Student('Василий', 'Васильев', 'м')
print(ivan < new_student, end='\n\n')

# Теперь студенты будут оценивать лекторов
# Иван оценивает лектора по Python
ivan.rate_lecturer(python_lecturer, 'Python', 10)
ivan.rate_lecturer(python_lecturer, 'Python', 6)
ivan.rate_lecturer(python_lecturer, 'Python', 8)
print(python_lecturer, end='\n\n')

# Маша не сможет оценить лектора по Python, потому что уже закончила курс (вероятно она оценивала когда-то раньше)
mary.rate_lecturer(python_lecturer, 'Python', 1)
print(python_lecturer, end='\n\n')

# Иван оценивает лектора по GIT и Английскому
ivan.rate_lecturer(git_english_lecturer, 'Git', 10)
ivan.rate_lecturer(git_english_lecturer, 'Английский', 10)
ivan.rate_lecturer(git_english_lecturer, 'Python', 10)
print(git_english_lecturer.grades)  # GIT оценили, курс английского Иван уже закончил, а Python этот лектор не Читает
print(git_english_lecturer, end='\n\n')


# Маша оценивает лектора по GIT и Английскому, тут все в порядке
mary.rate_lecturer(git_english_lecturer, 'Git', 10)
mary.rate_lecturer(git_english_lecturer, 'Английский', 10)
print(git_english_lecturer.grades)
print(git_english_lecturer, end='\n\n')

# Маша и Иван не смогут оценить студентов или экспертов
mary.rate_lecturer(ivan, 'Git', 5)
ivan.rate_lecturer(english_reviewer, 'Python', 7)
print()

# Теперь можно сравнить наших лекторов друг с другом
print('Гит и английский преподают хуже Пайтона?', git_english_lecturer < python_lecturer)
print('Гит и английский преподают хуже или так же, как Пайтон?', git_english_lecturer <= python_lecturer)
print('Гит и английский преподают лучше или так же, как Пайтон?', git_english_lecturer >= python_lecturer)
print('Пайтон преподают не так же, как Гит и английский?', python_lecturer != git_english_lecturer)
print('Пайтон преподают так же, как Гит и английский?', python_lecturer == git_english_lecturer, end='\n\n')

# И со студентами и экспертами
print(git_english_lecturer < ivan)
print(python_lecturer < english_reviewer, end='\n\n')


def average_student_course_grade(students, course_name):
    filtered_students = [i for i in students if course_name in i.grades.keys()]
    count = 0
    for item in filtered_students:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    return round(count / len(filtered_students), 1)


print('Средняя оценка лекторов на курсе Английский -', average_student_course_grade(students_list, 'Английский'))
print('Средняя оценка лекторов на курсе Git -', average_student_course_grade(students_list, 'Git'))
print('Средняя оценка лекторов на курсе Python -', average_student_course_grade(students_list, 'Python'), end='\n\n')


def average_lecturer_course_grade(lecturers, course_name):
    filtered_lecturers = [i for i in lecturers if course_name in i.grades.keys()]
    count = 0
    for item in filtered_lecturers:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    return round(count / len(filtered_lecturers), 1)


print('Средняя оценка лекторов на курсе Git -', average_lecturer_course_grade(lecturer_list, 'Git'))
print('Средняя оценка лекторов на курсе Английский -', average_lecturer_course_grade(lecturer_list, 'Английский'))
print('Средняя оценка лекторов на курсе Python -', average_lecturer_course_grade(lecturer_list, 'Python'), end='\n\n')
