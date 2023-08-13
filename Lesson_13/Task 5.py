# Реалізуйте ітератор для перебору всіх ключів словника.

class DictKeysIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.key_list = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.key_list):
            raise StopIteration
        else:
            key = self.key_list[self.index]
            self.index += 1
            return key


dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)
