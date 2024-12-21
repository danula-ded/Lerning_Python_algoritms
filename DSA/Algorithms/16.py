# Даны две последовательности, требуется найти длину их
# наибольшей общей подпоследовательности.

from typing import TypeVar

T = TypeVar('T')


def find_lcs(first: list[T], second: list[T]) -> int:
    cache: list[list[int]] = [
        [0 for _ in range(len(second) + 1)]
        for _ in range(len(first) + 1)
    ]

    for first_index in range(len(first)):
        for second_index in range(len(second)):
            if first[first_index] == second[second_index]:
                cache[first_index + 1][second_index + 1] = cache[first_index][second_index] + 1
            else:
                new_value: int = max(
                    cache[first_index + 1][second_index],
                    cache[first_index][second_index + 1],
                )
                cache[first_index + 1][second_index + 1] = new_value

    return cache[-1][-1]


# print(find_lcs([1, 4, 2, 4, 3], [1, 2, 3]))
