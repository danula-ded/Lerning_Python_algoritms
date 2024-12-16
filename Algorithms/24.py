# Дана строка S с повторяющимися буквами.
# Переставить буквы таким образом, чтобы одинаковые буквы не стояли рядом.

# Примечание: строка содержит только строчные латинские буквы и
# может иметь множество решений. Верните любое из них.


def create_new_string(text: str) -> None | str:
    text_length = len(text)
    chars = ['' for _ in range(text_length)]

    chars_count: dict[str, int] = {}
    for char in text:
        chars_count[char] = chars_count.get(char, 0) + 1

    sorted_chars = sorted(chars_count.items(), key=lambda x: x[1], reverse=True)

    if sorted_chars[0][1] > text_length // 2:
        return None

    even_index = 0
    odd_index = 1

    for char, count in sorted_chars:
        for _ in range(count):
            if even_index < text_length:
                chars[even_index] = char
                even_index += 2
            else:
                chars[odd_index] = char
                odd_index += 2

    result = ''.join(chars)

    return result


input_str = 'aaa'
output_str = create_new_string(input_str)
print(f'Input: {input_str}')
print(f'Output: {output_str}')
