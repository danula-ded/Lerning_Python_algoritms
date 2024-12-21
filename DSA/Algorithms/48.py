# Найти Z-функцию для строки.


# Что такое z-функция? ↓
# https://ru.algorithmica.org/cs/string-searching/z-function/


# Наивная реализация O(n^2)
def z_function(string: str) -> list[int]:
    length = len(string)
    result: list[int] = [0] * length

    for index in range(1, length):
        # Индекс последнего элемента второй последовательности
        # меньше длины (Чтоб не получить IndexError)
        # И значение префикса равняется значению второй последовательности
        while (index + result[index] < length) \
                and (string[result[index]] == string[index + result[index]]):
            result[index] += 1
    return result


# Норм реализация O(n)
def z_function_improved(string: str) -> list[int]:
    length = len(string)
    result = [0] * length
    (left_pointer, right_pointer) = (0, 0)

    for index in range(1, length):
        # Если index в промежутке [left_pointer, right_pointer]
        if index < right_pointer:
            # объяснение формулы (Его реально осилить) ↓
            # https://e-maxx.ru/algo/z_function
            # Вкратце, 1 -> Если вылазит, 2 -> одинаковые значения
            result[index] = min(right_pointer - index, result[index - left_pointer])

        # Эта часть из наивного
        while index + result[index] < length and string[result[index]] == string[index + result[index]]:
            result[index] += 1

        if index + result[index] > right_pointer:
            left_pointer = index
            right_pointer = index + result[index]

    return result


# Применение
def find_index(text: str, pattern: str) -> int:
    z_values: list[int] = z_function_improved(pattern + '~' + text)

    for index in range(len(pattern) + 1, len(text) + len(pattern) + 1):
        if z_values[index] == len(pattern):
            return index - len(pattern) - 1

    return -1

# for string in ('aaaaa', 'aaabaab', 'abacaba', 'abcabc'):
#     print(z_function_improved(string))

# print(find_index('aaaa, dfdfd, asdfasdf, 3423', '34'))
