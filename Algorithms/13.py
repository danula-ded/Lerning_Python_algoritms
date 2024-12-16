# Реализовать алгоритм быстрой сортировки.


# Simplest realization, but it's not O(1) for memory
def quick_sort1(numbers: list[int]) -> list[int]:
    if len(numbers) < 1:
        return numbers

    pivot: int = numbers[0]

    smaller = [number for number in numbers if number < pivot]
    equal = [number for number in numbers if number == pivot]
    bigger = [number for number in numbers if number > pivot]

    return quick_sort1(smaller) + equal + quick_sort1(bigger)


# print(quick_sort1([3, 45, 12, 5, 6, 3, 1, 34, 6, -0, 0, 34, -34345]))


# "In place", it's better
# https://youtu.be/WprjBK0p6rw?si=5pgoxQGxIvSL6vkD
def partition(numbers: list[int], start: int, end: int) -> int:
    pivot: int = numbers[end]
    first_pointer: int = start - 1

    for second_pointer in range(start, end + 1):
        if numbers[second_pointer] <= pivot:
            first_pointer += 1

            numbers[first_pointer], numbers[second_pointer] = (
                numbers[second_pointer],
                numbers[first_pointer],
            )

    return first_pointer


def quick_sort2(numbers: list[int]) -> None:
    def inner(numbers: list[int], start: int, end: int) -> None:
        if start >= end:
            return

        pivot = partition(numbers, start, end)
        inner(numbers, start, pivot - 1)
        inner(numbers, pivot + 1, end)

    inner(numbers, 0, len(numbers) - 1)


# numbers = [23, 43, 1, 2, 3, 5, 3, 2, 5, -3434, -3434, 0, -34, 2]
# quick_sort2(numbers)
# print(numbers)
