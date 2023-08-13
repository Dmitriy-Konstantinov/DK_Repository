# Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо та зправа наліво)
# з заданого списку слів.

class PalindromeIterator:
    def __init__(self, palindrome):
        self.palindrome = palindrome
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.palindrome):
            if self.palindrome[self.index] == self.palindrome[self.index][::-1]:
                result = self.palindrome[self.index]
                self.index += 1
                return result
            else:
                self.index += 1

        raise StopIteration


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)
