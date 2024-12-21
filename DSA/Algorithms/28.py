# Дан ориентированный невзвешенный граф. Определить является ли данный граф ациклическим.


def has_cycle(graph: list[list[int]]):
    # Функция для выполнения поиска в глубину (DFS)
    def dfs(node, visited, rec_stack):
        visited[node] = True  # Помечаем узел как посещенный
        rec_stack[node] = True  # Добавляем узел в стек рекурсии

        # Рекурсивно обходим все соседние узлы
        for neighbor in graph[node]:
            if not visited[neighbor]:  # Если соседний узел не посещен, запускаем поиск в глубину для него
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:  # Если соседний узел уже в стеке, значит образуется цикл
                return True

        rec_stack[node] = False  # Убираем узел из стека рекурсии
        return False

    # Инициализируем списки для хранения информации о посещенных узлах и стека рекурсии
    visited = [False for _ in range(len(graph))]
    rec_stack = [False for _ in range(len(graph))]

    # Запускаем поиск в глубину для каждого узла
    for node in range(len(graph)):
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True  # Если обнаружен цикл, возвращаем True

    return False  # В случае, если цикл не найден, возвращаем False

print(has_cycle([[1,2], [3,4], [5,6], [], [], [], [2]]))