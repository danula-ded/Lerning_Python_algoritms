# Дан список цифр (значения от 0 до 9), найти минимальную
# возможную сумму двух чисел, составленных из цифр в списке.
# Все цифры должны быть использованы.

# Любое сочетание цифр может быть использовано для составления
# чисел. Ведущие нули разрешены.

# Если составить 2 числа невозможно (например, n==0),
# тогда "сумма" - это значение единственно возможного числа.


# В оптимальности вообще не уверен, но вроде работает. O(n * log(n)) - В основном только сортировка

from itertools import count


def find_min_sum(digits: list[int]) -> int:
    match(digits):
        case []: return 0
        case [_]: return digits[0]

    result: int = 0
    digits = sorted(digits)

    for power in count():
        if not digits:
            break

        result += sum(digits[-2:]) * 10**power
        digits = digits[:-2]

    return result


print(find_min_sum([4, 5, 8, 7, 3]))
