# Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і список оцінок.
# Реалізуйте метод __len__, який повертає кількість оцінок студента.
# Створіть список студентів і відсортуйте його за кількістю оцінок.

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __len__(self):
        return len(self.marks)

    def __gt__(self, other):
        return len(self.marks) > len(other.marks)

    def __str__(self):
        return f'{self.name} {self.surname} has {len(self.marks)} marks'


axel = Student('Axel', 'Stone', [74, 99, 95, 88])
adam = Student('Adam', 'Hunter', [77, 74, 66])
blaze = Student('Blaze', 'Fielding', [75, 79, 78, 76, 68])

students = [axel, adam, blaze]
students.sort(reverse=True)

for item in students:
    print(item)
