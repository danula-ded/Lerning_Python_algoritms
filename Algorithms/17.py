# Дано N золотых слитков массой  m(1), ..., m(N)
# Ими наполняют рюкзак, который выдерживает вес не более M.
# Можно ли набрать вес в точности M?

# Смотри в extra_task backpack, иначе вряд ли поймёшь

# Не уверен, что это решение оптимально


def can_fill_out_backpack(weights: list[int], capacity: int) -> bool:
    things_count: int = len(weights)
    cache: list[list[int]] = [
        [0 for _ in range(capacity + 1)]
        for _ in range(things_count + 1)
    ]

    for thing_index in range(things_count):
        for capacity_value in range(1, capacity + 1):
            if weights[thing_index] > capacity_value:
                cache[thing_index + 1][capacity_value] = cache[thing_index][capacity_value]
            else:
                new_value: int = max(
                    cache[thing_index][capacity_value],
                    weights[thing_index] + cache[thing_index][capacity_value - weights[thing_index]]
                )

                if new_value == capacity:
                    return True

                cache[thing_index + 1][capacity_value] = new_value

    return False

# print(can_fill_out_backpack([3, 4, 5], 8))
# print(can_fill_out_backpack([8], 8))
# print(can_fill_out_backpack([4, 1, 2, 1], 8))
# print(can_fill_out_backpack([2, 2, 3, 7], 8))
