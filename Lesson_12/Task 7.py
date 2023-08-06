# Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції протягом певного періоду
# часу. Декоратор повинен приймати два параметри `max_calls` та `period`. Перший парметр - максимальна кількість
# допустимих викликів функції. Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів.
# Вам допоможе модуль `datetime` для вирішення цієї задачі.

from datetime import datetime, timedelta
import time


def rate_limit(max_calls, period):

    def decorator(func):
        call_times = []

        def inner(*args, **kwargs):
            now = datetime.now()
            new_call_times = []

            for item in call_times:
                if now - item <= period:
                    new_call_times.append(item)
            call_times[:] = new_call_times

            if len(call_times) >= max_calls:
                raise Exception('Rate limit exceeded')

            call_times.append(now)
            return func(*args, **kwargs)

        return inner

    return decorator


@rate_limit(max_calls=5, period=timedelta(seconds=10))
def my_function():
    print("This function is rate-limited!")


for x in range(6):
    try:
        my_function()
    except Exception as e:
        print(e)
