def get_multiplied_digits(number):
    result = 1
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        result = first * get_multiplied_digits(int(str_number[1::]))
    else:
        result = first
    return result

print(get_multiplied_digits(40203))