# Розробіть клас Library для представлення бібліотеки. А також класс Book для представлення книги. Класс Library повинен
# мати атрибут books зі списком книжок. Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки. Реалізуйте метод __str__, який виводить список книг
# у бібліотеці. Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        books_list = '\n'.join(str(book) for book in self.books)
        return books_list


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f'{self.title} by {self.author}, {self.publication_year} year'


dune = Book('Dune', 'Frank Herbert', 1965)
lord_of_the_rings = Book('Lord of the Rings', 'John Tolkien', 1954)
harry_potter = Book('Harry Potter', 'Joanne Rowling', 1997)

my_library = Library()

my_library.add_book(dune)
my_library.add_book(lord_of_the_rings)
my_library.add_book(harry_potter)

print(my_library)
