# Реализовать сортировку списка строк на основе хеширования.

def polynomial_hash(string: str, p: int) -> int:
    result = 0
    power = 0

    for char in string:
        result += p**power * ord(char)
        power += 1

    return result


def sorted_strings_by_hash(strings: list[str]) -> list[str]:
    cache: dict[int, list[str]] = {}
    result: list[str] = []

    for string in strings:
        string_hash = polynomial_hash(string, 3)
        cache[string_hash] = cache.get(string_hash, []) + [string]

    for string_hash in sorted(cache.keys()):
        result.extend(cache[string_hash])

    return result


# strings = ['sirius', 'nono', 'test', 'nono']

# for string in strings:
#     print(polynomial_hash(string, 3))

# print(sorted_strings_by_hash(strings))
