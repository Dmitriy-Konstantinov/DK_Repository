import random


words = ['феод', 'ликвидирование', 'кровожадность', 'светокопирование', 'перемещение', 'расстреливание', 'скорнячка',
         'отстранение', 'племянница', 'турбулентность']
chosen_word = random.choice(words)
win = list('*' * len(chosen_word))
print(f'Загаданное слово состоит из {len(win)} букв')
tries = int(input('Укажите количество попыток: '))
counter = 0

while '*' in win and counter < tries:
    guess = input('Введите вашу букву или слово: ').lower()

    if len(guess) == 1:
        if guess in chosen_word:
            iterator = 0
            for char in chosen_word:
                if char == guess:
                    win[iterator] = char
                iterator += 1
        else:
            print('Такой буквы нет')
            counter += 1

        print(''.join(win))
    elif len(guess) > 1:
        if guess == chosen_word:
            print('Поздравляю, вы выиграли супер приз: Автомобиль!')
            break
        else:
            print('Это неправильное слово')
            counter += 1

if '*' in win and counter == tries:
    print('Количество попыток исчерпано. Вы проиграли.')
