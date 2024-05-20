def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < n and arr[left] < arr[largest]:
            largest = left

        if right < n and arr[right] < arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            heapify(arr, n, largest)
    
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  
        heapify(arr, i, 0)

# Пример использования
arr = [7, 1, 9, 3, 6, 5, 8]
heap_sort(arr)
print("Отсортированный массив:", arr)
