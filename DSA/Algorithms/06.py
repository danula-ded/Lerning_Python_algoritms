# Проверить, является ли число a простым.

from math import sqrt, floor


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    limit: int = floor(sqrt(number)) + 1

    for divider in range(2, limit):
        if number % divider == 0:
            return False

    return True

# for number in range(0, 13 + 1):
#     print(number, is_prime(number))
