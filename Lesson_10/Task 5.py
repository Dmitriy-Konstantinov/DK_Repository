# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

f = open('Lorem ipsum.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nPhasellus\nvitae.')
f.close()

f = open('Lorem ipsum.txt')
s1 = str(f.read())
words = s1.split()
print(f'Файл состоит из {len(words)} слов')
f.close()
