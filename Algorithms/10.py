# Дан список целых чисел arr. Реализовать сортировку вставками
# (без использования бинарного поиска), в качестве результата вернуть
# количество перестановок выполненных в процессе сортировки.


# insertion sort
def count_swipes_in_insertion_sort(array: list[int]) -> int:
    numbers: list[int] = array.copy()
    count: int = 0

    for current_index in range(1, len(numbers)):
        for index in range(current_index, 0, -1):
            if numbers[index] < numbers[index - 1]:
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                count += 1

    return count


# print(count_swipes_in_insertion_sort([5, 3, 4, 2, 7]))
