# Даны два числа a и b, представленные в виде строк.
# Найдите произведение этих чисел и верните его в виде строки.

# TODO It can be written better

# private
def add_big_numbers(first_number: str, second_number: str) -> str:
    result: str = ''
    rest: int = 0

    (min_number, max_number) = (
        (first_number, second_number)
        if len(first_number) < len(second_number)
        else (second_number, first_number)
    )

    for index in range(-1, -len(max_number) - 1, -1):
        try:
            min_number_value = int(min_number[index])
        except IndexError:
            min_number_value = 0

        max_number_value = int(max_number[index])

        numbers_sum = min_number_value + max_number_value + rest
        result = str(numbers_sum % 10) + result
        rest = numbers_sum // 10

    if rest:
        result = str(rest) + result

    return result

# private
def multiply_big_number_and_small(big_number: str, small_number: str) -> str:
    result: str = ''
    rest: int = 0

    for index in range(-1, -len(big_number) - 1, -1):
        multi = int(big_number[index]) * int(small_number) + rest
        result = str(multi % 10) + result
        rest = multi // 10

    if rest:
        result = str(rest) + result

    return result

# public
def multiply_numbers(first_number: str, second_number: str) -> str:
    # TODO check negative numbers

    result: str = '0'
    swipe: int = 0

    (min_number, max_number) = (
        (first_number, second_number)
        if len(first_number) < len(second_number)
        else (second_number, first_number)
    )

    for index in range(-1, -len(min_number) - 1, -1):
        multiply = multiply_big_number_and_small(max_number, min_number[index])
        result = add_big_numbers(result, f'{multiply}{'0' * swipe}')
        swipe += 1

    return result

# adding = add_big_numbers('1234', '9234')
# multiply = multiply_big_number_and_small(adding, '9')
# print(multiply_numbers('34543534', '345345345345345435'))
