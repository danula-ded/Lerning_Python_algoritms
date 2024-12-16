# Реализовать полиномиальную хеш-функцию для строк.

# Самая простая реализация


def polynomial_hash(string: str, p: int) -> int:
    result = 0
    power = 0

    for char in string:
        result += p**power * ord(char)
        power += 1

    return result


# print(polynomial_hash('sirius', 3))
