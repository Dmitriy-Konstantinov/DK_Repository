# Реалізуйте програму, яка копіює вміст одного файлу в інший.

f = open('Lorem ipsum.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nPhasellus\nvitae.')
f.close()

f = open('Copy file.txt', 'w')
f.close()

f = open('Lorem ipsum.txt')
copy_text = f.read()
f.close()

cf = open('Copy file.txt', 'w')
cf.write(copy_text)
cf.close()
