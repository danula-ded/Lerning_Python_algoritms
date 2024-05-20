def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# Пример использования:
arr = [12, 34, 54, 2, 3]
bubble_sort(arr)
print("Отсортированный массив:", arr)
