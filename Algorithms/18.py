# Определите расстояние Левенштейна для двух данных строк s1 и s2.

# https://youtu.be/903VbCD7uBw?si=3mW6HscFtT1Ur9Wl
# https://habr.com/ru/articles/676858/


def calculate_levenshtein_distance(first: str, second: str) -> int:
    cache: list[list[int]] = [
        [0 for _ in range(len(second) + 1)]
        for _ in range(len(first) + 1)
    ]

    for second_index in range(1, len(second) + 1):
        cache[0][second_index] = second_index

    for first_index in range(1, len(first) + 1):
        cache[first_index][0] = first_index

    for first_index in range(1, len(first) + 1):
        for second_index in range(1, len(second) + 1):
            extra: int = 1 if first[first_index - 1] != second[second_index - 1] else 0

            new_value: int = min(
                cache[first_index - 1][second_index - 1] + extra,
                cache[first_index][second_index - 1] + 1,
                cache[first_index - 1][second_index] + 1,
            )
            cache[first_index][second_index] = new_value

    return cache[-1][-1]


# print(calculate_levenshtein_distance('ГИБРАЛТАР', 'ЛАБРАДОР'))
# print(calculate_levenshtein_distance('DISTANCE', 'EDITING'))

