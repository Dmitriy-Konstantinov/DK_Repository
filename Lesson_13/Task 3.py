# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.

class StringIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


string = 'Hello, World!'
str_iter = StringIterator(string)
for char in str_iter:
    print(char)
