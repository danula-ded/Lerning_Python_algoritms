def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i  # Возвращаем индекс элемента, если найден
    return -1  # Возвращаем -1, если элемент не найден

# Пример использования
arr = [7, 1, 9, 3, 6, 5, 8]
target = 6
index = linear_search(arr, target)
if index != -1:
    print(f"Элемент {target} найден в массиве на позиции {index}.")
else:
    print(f"Элемент {target} не найден в массиве.")
