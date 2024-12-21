# Найти количество простых чисел в диапазоне от [0, n].

# Тут, кста, используется решето Эратосфена

def find_count_of_prime_number(end: int) -> int:
    if end < 2:
        return 0

    count: int = 0
    numbers: list[int] = [number for number in range(0, end + 1)]
    numbers[1] = 0

    for number in numbers:
        if number == 0:
            continue

        count += 1

        for index in range(number * 2, end + 1, number):
            numbers[index] = 0

    return count


# for number in range(25, 50):
#     print(number, find_count_of_prime_number(number))
