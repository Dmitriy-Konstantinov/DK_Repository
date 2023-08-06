# Створіть простий декоратор логування log_func, який буде прінтити будь яке повідомлення перед визовом декорованої
# функції, та після.

def log_func(func):

    def inner():
        print('Message before a function')
        func()
        print('Message after a function')

    return inner


@log_func
def list_to_string():
    fruits_list = ['apple', 'banana', 'orange']
    fruits_string = '\n'.join(fruits_list)
    print(fruits_string)


list_to_string()
