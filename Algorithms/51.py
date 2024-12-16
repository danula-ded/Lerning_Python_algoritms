# Найти и вернуть все индексы начала вхождения строки pat в строку text.

# Тут можно использовать либо наивный алгоритм,
# либо z-функцию, либо Алгоритм Кнута — Морриса - Пратта, либо через хеш
# Можно понадеяться на наивный, но лучше рассмотреть z-функцию


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


def find_indexes(text: str, pattern: str) -> list[int]:
    z_values: list[int] = z_function_improved(pattern + '~' + text)
    result: list[int] = []

    for index in range(len(pattern) + 1, len(text) + len(pattern) + 1):
        if z_values[index] == len(pattern):
            result.append(index - len(pattern) - 1)

    return result


# print(find_indexes('ababababcsdfdsfab', 'ab'))
