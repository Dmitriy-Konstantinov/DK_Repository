# Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок.
# Створіть статік метод який буде приймати список книжок та рік, та повертати кількість книжок з цього списку які були
# опубліковані у цьому році.

class Book:
    def __init__(self, title, author, publication_year, pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages

    @staticmethod
    def book_quantity_by_year(books: list, year):
        counter = 0
        for item in books:
            if item.publication_year == year:
                counter += 1
        return counter


book_1 = Book('Book 1', 'Leonardo', 1997, 248)
book_2 = Book('Book 2', 'Raphael', 1992, 288)
book_3 = Book('Book 3', 'Donatello', 1995, 478)
book_4 = Book('Book 4', 'Michelangelo', 1992, 329)

books_list = [book_1, book_2, book_3, book_4]
print(Book.book_quantity_by_year(books_list, 1992))
