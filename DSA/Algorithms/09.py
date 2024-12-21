# Дан список целых чисел arr. Реализовать сортировку простыми обменами,
# в качестве результата вернуть количество перестановок выполненных в процессе сортировки.

# Bubble sort

def count_swipes_in_bubble_sort(array: list[int]) -> int:
    numbers: list[int] = array.copy()
    count: int = 0

    for iteration_index in range(len(numbers) - 1):
        had_swipe: bool = False #  for optimization

        for index in range(len(numbers) - 1 - iteration_index):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                had_swipe = True
                count += 1

        if not had_swipe:
            break

    return count


# print(count_swipes_in_bubble_sort([5, 3, 4, 2, 5, 6, 7, -34, 4, 3284324, -3248]))
