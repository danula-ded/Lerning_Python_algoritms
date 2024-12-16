# Найти минимальное покрывающее дерево для заданного графа. Вывести список его ребер и суммарный вес.



import heapq

# юзаю алгоритм прима (внизу описание построчно)
def prim(graph):
    mst = []
    nodes = set(graph)
    start_node = nodes.pop()
    visited = {start_node}
    edges = [
        (cost, start_node, to)
        for to, cost in graph[start_node]
    ]
    heapq.heapify(edges)
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            
            for to_next, cost in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst

graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)]
}

print(prim(graph))

# 1. import heapq: Мы импортируем модуль heapq, который предоставляет функции и алгоритмы для работы с "кучами" (heap), минимальными очередями.
# 2. def prim(graph): Это объявление функции prim, которая принимает на вход граф в виде словаря, где ключи - это вершины, а значения - это список смежных вершин с их стоимостями.
# 3. mst = []: Мы создаем пустой список mst, который будет представлять минимальное остовное дерево (minimum spanning tree).
# 4. nodes = set(graph): Мы создаем множество nodes из вершин графа.
# 5. start_node = nodes.pop(): Мы извлекаем произвольную стартовую вершину из множества вершин.
# 6. visited = {start_node}: Мы создаем множество visited, содержащее только стартовую вершину, чтобы отслеживать посещенные вершины.
# 7. edges = [(cost, start_node, to) for to, cost in graph[start_node]]: Мы создаем список ребер edges, где каждое ребро представляется в виде кортежа (cost, start_node, to) для каждой смежной вершины стартовой вершины. Кортежи сразу добавляются в список с помощью генератора списка.
# 8. heapq.heapify(edges): Мы преобразуем список edges в минимальную кучу (min-heap) с помощью функции heapify из модуля heapq.
# 9. while edges: ...: Мы начинаем цикл, который будет продолжаться, пока у нас есть ребра в куче edges.
# 10. cost, frm, to = heapq.heappop(edges): Мы извлекаем ребро с минимальной стоимостью из кучи edges.
# 11. if to not in visited: ...: Мы проверяем, посещена ли вершина to.
# 12. visited.add(to): Мы добавляем вершину to в множество посещенных вершин.
# 13. mst.append((frm, to, cost)): Мы добавляем ребро в список mst, представляя его в виде кортежа (frm, to, cost).
# 14. for to_next, cost in graph[to]: ...: Мы итерируемся по смежным вершинам вершины to.
# 15. if to_next not in visited: ...: Мы проверяем, посещена ли смежная вершина to_next.
# 16. heapq.heappush(edges, (cost, to, to_next)): Если смежная вершина не посещена, мы добавляем соответствующее ребро в кучу edges.
# 17. return mst: Мы возвращаем список mst, представляющий минимальное остовное дерево.

