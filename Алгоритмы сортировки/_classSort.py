class Sort:
    def __init__(self, arr):
        self.arr = arr.copy()

    #сортировка выбором
    def selection_sort(self):
        arr = self.arr
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    #сортировка вставкой
    def insertion_sort(self):
        arr = self.arr
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    #сортировка Шелла
    def shell_sort(self):
        arr = self.arr
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr
    
    #сортировка слиянием
    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.arr
        if len(arr) > 1: 
            mid = len(arr) // 2
            left = arr[:mid] 
            right = arr[mid:]
            self.merge_sort(left) 
            self.merge_sort(right) 
            i = j = k = 0
            while i < len(left) and j < len(right): 
                if left[i] < right[j]: 
                    arr[k] = left[i] 
                    i += 1
                else: 
                    arr[k] = right[j] 
                    j += 1
                k += 1
            while i < len(left): 
                arr[k] = left[i] 
                i += 1
                k += 1
            while j < len(right): 
                arr[k] = right[j] 
                j += 1
                k += 1
        return arr

    #сортировка обменом(пузырьком)
    def bubble_sort(self):
        arr = self.arr
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    
    #Турнираная сортировка 
    def tournament_sort(self):
        arr = self.arr
        n = len(arr)
        tree = [None] * (2 * n)
        # Построение "дерева" турнира
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        # Выбор максимального элемента из корня дерева
        result = []
        while len(result) < n:
            result.append(tree[1])
            # Замена выбранного максимального элемента в дереве на минимальное значение
            j = 1
            while j < n:
                if tree[j] == tree[j * 2]:
                    j = j * 2
                else:
                    j = j * 2 + 1
            tree[j] = float('-inf')  # Замена на минимальное значение
            # Перестройка дерева
            j //= 2
            while j > 0:
                tree[j] = max(tree[j * 2], tree[j * 2 + 1])
                j //= 2
        return result


    #Пирамидная сортировка
    def heap_sort(self):
        arr = self.arr
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
        return arr



    
# Пример использования:
arr = [64, 25, 12, 22, 11]
sort = Sort(arr)




print("Сортировка выбором:", sort.selection_sort())
print("Сортировка вставкой:", sort.insertion_sort())
print("Сортировка Шелла:", sort.shell_sort())
print("Сортировка слиянием:", sort.merge_sort())
print("сортировка обменом(пузырьком):", sort.bubble_sort())
print("Турнирная сортировка:", sort.tournament_sort())
print("Пирамидальная сортировка:", sort.heap_sort())
print(arr)
