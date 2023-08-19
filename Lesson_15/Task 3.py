def reverse_string(input_string):
    if len(input_string) <= 1:
        return input_string

    return reverse_string(input_string[1:]) + input_string[0]


print(reverse_string("Hello"))
