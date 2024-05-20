def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Искомый элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится в правой половине
        else:
            right = mid - 1  # Искомый элемент находится в левой половине
    
    return -1  # Искомый элемент не найден

# Пример использования
arr = [1, 3, 5, 6, 7, 9, 10]
target = 6
index = binary_search(arr, target)
if index != -1:
    print(f"Элемент {target} найден в массиве на позиции {index}.")
else:
    print(f"Элемент {target} не найден в массиве.")
