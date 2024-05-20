class Search:
    def __init__(self, data):
        self.data = data

    def sequential_search(self, target):
        for i, value in enumerate(self.data):
            if value == target:
                return i
        return -1

    def binary_search(self, target):
        low = 0
        high = len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def fibonacci_search(self, target):
        fibM2 = 0
        fibM1 = 1
        fibM = fibM2 + fibM1
        n = len(self.data)
        while fibM < n:
            fibM2 = fibM1
            fibM1 = fibM
            fibM = fibM2 + fibM1
        offset = -1
        while fibM > 1:
            i = min(offset + fibM2, n-1)
            if self.data[i] < target:
                fibM = fibM1
                fibM1 = fibM2
                fibM2 = fibM - fibM1
                offset = i
            elif self.data[i] > target:
                fibM = fibM2
                fibM1 = fibM1 - fibM2
                fibM2 = fibM - fibM1
            else:
                return i
        if fibM1 and self.data[offset+1] == target:
            return offset + 1
        return -1

    def interpolation_search(self, target):
        low = 0
        high = len(self.data) - 1
        while low <= high and target >= self.data[low] and target <= self.data[high]:
            if low == high:
                if self.data[low] == target:
                    return low
                return -1
            pos = low + ((high - low) // (self.data[high] - self.data[low]) * (target - self.data[low]))
            if self.data[pos] == target:
                return pos
            if self.data[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        return -1

# Пример использования
data1 = [10, 20, 30, 40, 50, 60]
data2 = [1, 3, 5, 7, 9, 11, 13]

search1 = Search(data1)
search2 = Search(data2)

# Последовательный поиск
print("Последовательный поиск:", search1.sequential_search(30))

# Бинарный поиск
print("Бинарный поиск:", search1.binary_search(30))

# Фибоначчиев поиск
print("Фибоначчиев поиск:", search1.fibonacci_search(30))

# Интерполяционный поиск
print("Интерполяционный поиск:", search1.interpolation_search(30))

print("-----------------------------")
# Последовательный поиск
print("Последовательный поиск:", search2.sequential_search(9))

# Бинарный поиск
print("Бинарный поиск:", search2.binary_search(9))

# Фибоначчиев поиск
print("Фибоначчиев поиск:", search2.fibonacci_search(9))

# Интерполяционный поиск
print("Интерполяционный поиск:", search2.interpolation_search(9))
