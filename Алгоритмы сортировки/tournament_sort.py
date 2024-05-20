def tournament_sort(arr):
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


arr = [7, 1, 9, 3, 6, 5, 8]
sorted_arr = tournament_sort(arr)
print("Отсортированный массив:", sorted_arr)

