# Реализуйте алгоритм быстрого возведения числа a в степень b.

def fast_power(number: int, power: int) -> int:
    current_power: int = power
    multi: int = number
    result: int = 1

    while current_power:
        if current_power % 2 == 0:
            current_power /= 2 # type: ignore
            multi **= 2
        else:
            current_power -= 1
            result *= multi

    return result


# for power in range(2, 10 + 1):
#     print(fast_power(2, power))
