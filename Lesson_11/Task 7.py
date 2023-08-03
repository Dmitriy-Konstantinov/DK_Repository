# Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для відстеження кількості студентів.
# Для цього змінюйте значення атрибуту класу у методі __init__ .
# Та створіть клас метод для виведення загальної кількості студентів.

class Student:
    students_quantity = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.students_quantity += 1

    @classmethod
    def total_students(cls):
        return print(f'Total students in a group: {cls.students_quantity}')


bruce = Student('Bruce', 'Wayne')
Student.total_students()
james = Student('James', 'Howlett')
Student.total_students()
johnny = Student('Johnny', 'Blaze')
Student.total_students()
