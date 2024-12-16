# Найти k-тое по счету простое число. Число 2 считать простым числом с номером 1.

def find_prime_number_by_index(index: int) -> int:
    if index < 1:
        raise ValueError('The index has to be more 0!')

    prime_numbers: list[int] = []
    current_number: int = 2

    while True:
        for prime_number in prime_numbers:
            if current_number % prime_number == 0:
                break
        else:
            prime_numbers.append(current_number)

            if len(prime_numbers) == index:
                return current_number

        current_number += 1


# for number in range(1, 10 + 1):
#     print(find_prime_number_by_index(number))
