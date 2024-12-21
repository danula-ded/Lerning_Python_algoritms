# Дана строка S состоящая из открывающихся и закрывающихся скобок
# '(' и ')'. Найти длину наибольшей правильной
# последовательности скобок.

# Последовательность скобок верна если:
#       Для каждой открытой скобки есть закрытая
#       Открытые скобки должны закрываться в соответствующем порядке.


from collections import deque


def count_correct_brackets(brackets: str) -> int:
    BRACKETS: dict[str, str] = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    ERROR_VALUE: int = -1

    count: int = 0
    stack = deque[str]()

    for current_bracket in brackets:
        if current_bracket in BRACKETS.keys():
            stack.append(current_bracket)
            count += 1
        else:
            if not stack:
                return ERROR_VALUE

            prev_bracket: str = stack.pop()

            if BRACKETS[prev_bracket] != current_bracket:
                return ERROR_VALUE

    if stack:
        return ERROR_VALUE

    return count


# print(count_correct_brackets('{((()))[][){}{}}'))
