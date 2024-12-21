# Найти префикс-функцию для строки.

# Сразу эффективный, потому что рассматривать наивный со сложностью O(n^3)
# Просто бессмысленно

# Нормальное объяснение, но много воды
# https://youtu.be/xAYmgdB-8Fg?si=BrmGg0OtZlVifKQ0

def prefix_function(string: str) -> list[int]:
    length = len(string)
    result = [0] * length
    i = 1
    j = 0

    while i < length:
        if string[i] == string[j]:
            j += 1
            result[i] = j
            i += 1
        else:
            if j != 0:
                j = result[j - 1]
            else:
                result[i] = 0
                i += 1

    return result


# Алгоритм Кнута — Морриса - Пратта, если нужно будет
# https://youtu.be/Vncv1JbOVwg?si=BRuI5n8794_s0Vfa
