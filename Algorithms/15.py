# Вычислите n-й член последовательности, заданной формулами:
# a(2n) = a(n) + a(n - 1),
# a(2n + 1) = a(n) - a(n - 1),
# a(0) = a(1) = 1

# динамическое программирование мемоизация

from itertools import count


def calculate_element(element_number: int) -> int:
    cache: dict[int, int] = { 0: 1, 1: 1, }

    for index in count(1):
        needed_element: int | None = cache.get(element_number)

        if needed_element is not None:
            return needed_element

        cache[2 * index] = cache[index] + cache[index - 1]
        cache[2 * index + 1] = cache[index] - cache[index - 1]


    return -1 # для типизации, тк значение всегда будет возращаться из цикла (100%)


# print(calculate_element(10000))
