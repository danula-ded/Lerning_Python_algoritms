# Даны два сортированных списка arr1 и arr2.
# Выполнить их слияние так, чтобы полученный список так же был сортирован.

def merge(first_numbers: list[int], second_numbers: list[int]) -> list[int]:
    result: list[int] = []
    first_pointer: int = 0
    second_pointer: int = 0

    while first_pointer < len(first_numbers) and second_pointer < len(second_numbers):
        first_number: int = first_numbers[first_pointer]
        second_number: int = second_numbers[second_pointer]

        if first_number < second_number:
            result.append(first_number)
            first_pointer += 1
        else:
            result.append(second_number)
            second_pointer += 1

    if first_pointer != len(first_numbers):
        result.extend(first_numbers[first_pointer:])
    else:
        result.extend(second_numbers[second_pointer:])

    return result


# print(merge([1, 2, 89, 98, 984398, 8943843], [1, 3, 4, 5, 6]))


# Merge sort without recursion

def merge_sort(array: list[int]) -> list[int]:
    numbers = array.copy()
    count: int = 1

    while count < len(numbers):
        for index in range(0, len(numbers) - count, count * 2):
            numbers[index:(index + 2 * count)] = merge(
                numbers[index:(index + count)],
                numbers[(index + count):(index + count * 2)],
            )

        count *= 2

    return numbers

# print(merge_sort([5, 4, 3, 1, 234, 234, 0, -43, 43, 2, 3]))
