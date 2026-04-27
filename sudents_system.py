class Student:
    def __init__(self, student_id, name, age, major, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.subjects = subjects
        self.grades = {}

    def add_or_update_grade(self, subject_index, grade):
        try:
            subject = self.subjects[subject_index]
            self.grades[subject] = grade
            print(f"Оценка по {subject} обновлена")
        except IndexError:
            print("Неверный выбор предмета")

    def show_subjects(self):
        print(f"Предметы для {self.major}:")
        for i, subj in enumerate(self.subjects):
            print(f"{i}. {subj}")

    def show_grades(self):
        if not self.grades:
            print("Оценок нет")
            return

        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

        print(f"GPA: {self.calculate_gpa():.2f}")

    def calculate_gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major}"


class StudentSystem:
    def __init__(self):
        self.students = []
        self.majors = {
            "IT": ["Programming", "Algorithms", "Databases"],
            "Economics": ["Microeconomics", "Macroeconomics", "Statistics"],
            "Engineering": ["Physics", "Mechanics", "Math"]
        }

    def show_majors(self):
        print("Доступные специальности:")
        for i, major in enumerate(self.majors.keys()):
            print(f"{i}. {major}")

    def get_major_by_index(self, index):
        majors = list(self.majors.keys())
        try:
            return majors[index]
        except IndexError:
            return None

    def add_student(self, student):
        self.students.append(student)
        print("Студент добавлен")

    def show_students(self):
        if not self.students:
            print("Список пуст")
            return
        for s in self.students:
            print(s)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print("Удалено")
        else:
            print("Не найден")

    def seed_data(self):
        s1 = Student("1", "Rinat", 20, "IT", self.majors["IT"])
        s1.grades = {"Programming": 90, "Algorithms": 85, "Databases": 88}

        s2 = Student("2", "Amanat", 19, "Economics", self.majors["Economics"])
        s2.grades = {"Microeconomics": 88, "Macroeconomics": 91, "Statistics": 92}

        s3 = Student("3", "Mars", 21, "Engineering", self.majors["Engineering"])
        s3.grades = {"Physics": 75, "Mechanics": 78, "Math": 80}

        s4 = Student("4", "Nuris", 22, "IT", self.majors["IT"])
        s4.grades = {"Programming": 95, "Algorithms": 90, "Databases": 89}

        s5 = Student("5", "Altynai", 20, "Economics", self.majors["Economics"])
        s5.grades = {"Microeconomics": 78, "Macroeconomics": 82, "Statistics": 85}

        self.students.extend([s1, s2, s3, s4, s5])




system = StudentSystem()
system.seed_data()

while True:
    print("\n1. Добавить студента")
    print("2. Показать всех")
    print("3. Найти студента")
    print("4. Удалить студента")
    print("5. Поставить/обновить оценку")
    print("6. Показать оценки студента")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        system.show_majors()
        try:
            major_index = int(input("Выбери номер специальности: "))
            major = system.get_major_by_index(major_index)

            if major is None:
                print("Неверный выбор")
                continue

            subjects = system.majors[major]

            sid = input("ID: ")
            name = input("Имя: ")
            age = int(input("Возраст: "))

            system.add_student(Student(sid, name, age, major, subjects))

        except ValueError:
            print("Ошибка ввода")

    elif choice == "2":
        system.show_students()

    elif choice == "3":
        sid = input("Введите ID: ")
        student = system.find_student(sid)
        print(student if student else "Не найден")

    elif choice == "4":
        sid = input("Введите ID: ")
        system.delete_student(sid)

    elif choice == "5":
        sid = input("ID студента: ")
        student = system.find_student(sid)

        if student:
            student.show_subjects()
            try:
                subject_index = int(input("Выбери номер предмета: "))
                grade = float(input("Оценка: "))
                student.add_or_update_grade(subject_index, grade)
            except ValueError:
                print("Ошибка ввода")
        else:
            print("Студент не найден")

    elif choice == "6":
        sid = input("ID студента: ")
        student = system.find_student(sid)

        if student:
            student.show_grades()
        else:
            print("Студент не найден")

    elif choice == "0":
        print("Выход...")
        break

    else:
        print("Неверный ввод")
