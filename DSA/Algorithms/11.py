# Дан сортированный список целых чисел arr и число x.
# Найти индекс, на котором будет расположено число x в списке,
# после его добавления в список в порядке сортировки.

# use binary search

from math import floor


def find_index(array: list[int], number: int) -> int:
    left_pointer: int = 0
    right_pointer: int = len(array) - 1

    while left_pointer <= right_pointer:
        middle_pointer: int = floor((left_pointer + right_pointer) / 2)

        if array[middle_pointer] == number:
            return middle_pointer
        elif array[middle_pointer] < number:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1

    return left_pointer


print(find_index([1, 2, 10, 14, 34, 65, 106], 34))
