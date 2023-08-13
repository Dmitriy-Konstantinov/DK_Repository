# Створіть ітератор, який перебирає всі парні числа з заданого діапазону.

class EvenRangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            if self.start % 2 == 0:
                result = self.start
                self.start += 2
                return result
            else:
                self.start += 1

        raise StopIteration


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)
